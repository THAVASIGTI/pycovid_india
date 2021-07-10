#!/usr/bin/python3

import requests, os, logging, json
from datetime import datetime, timedelta
from .util import *


class CovidInfo:
    def __init__(self):
        self.location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.time_stamp_path = os.path.join(self.location, TIME_STAMP_FILE_NAME)
        self.config_file_path = os.path.join(self.location, CONFIG_FILE_NAME)
        self.state_code_file_path = os.path.join(self.location, STATE_CODE_NAME)
        self.get_state_id = self.read_json(self.state_code_file_path)
        self.config_buff = self.read_json(self.config_file_path)
        self.state_id_count = len(self.get_state_id)
        self.ignore_ids = [AS_ON, UPDATED_ON, STATE_NAME_HI]
        self.ignore_vacc_ids = [VACCION_UPDATE_ON, VACCINE_LAST_UPDATE]
        self.MASTER_VACCINE_DICT = None
        self.MASTER_CASES_DICT = None
        self.origin(INIT)

    def cache(self):
        try:
            status = False
            if not os.path.isfile(self.time_stamp_path):
                with open(self.time_stamp_path, "w+") as fs:
                    fs.write(json.dumps({TIME_STAMP_KEY: round(datetime.timestamp(datetime.now()))}))
                fs.close()
                status = True
            else:
                nowDateStamp = round(datetime.timestamp(datetime.now()))
                with open(self.time_stamp_path, "r") as fs:
                    buffDict = json.load(fs)
                    storeDateStamp = buffDict[TIME_STAMP_KEY]
                    diffSceound = round(datetime.timestamp(datetime.fromtimestamp(storeDateStamp) + timedelta(hours=5)))
                    if int(nowDateStamp) > int(diffSceound):
                        with open(self.time_stamp_path, "w") as fss:
                            fss.write(json.dumps({TIME_STAMP_KEY: nowDateStamp}))
                        fss.close()
                        status = True
                fs.close()
            return status
        except Exception as e:
            logging.debug(e)
            return False

    def read_json(self, _path):
        try:
            status = None
            with open(_path, "r") as fs:
                status = json.load(fs)
            fs.close()
            return status
        except Exception as e:
            logging.debug(e)
            return None

    def fetch(self, _url):
        status = None
        try:
            loopCount = 0
            while True:
                if loopCount > 5:
                    break
                with requests.request(METHOD_GET, _url, headers=DEF_HEADERS, timeout=120) as req:
                    if req.status_code == 200:
                        status = req.json()
                req.close()
                return status
        except Exception as e:
            logging.debug(e)
            return None

    def get_state_covid_info(self, state_id):
        try:
            try:
                int(state_id)
            except Exception as e:
                logging.debug(e)
                return None
            if int(state_id) <= self.state_id_count:
                return (
                    self.origin(STATE_COVID_INFO, state_id)
                )
        except Exception as e:
            logging.debug(e)

    def get_covid_vaccine_last_update(self):
        try:
            return (
                self.origin(LAST_UPDATE_VACCINE)
            )
        except Exception as e:
            logging.debug(e)
            return None

    def get_state_covid_vaccine_info(self, state_id):
        try:
            try:
                int(state_id)
            except Exception as e:
                logging.debug(e)
                return None
            if int(state_id) <= self.state_id_count:
                return (
                    self.origin(STATE_COVID_VACCINE_UPDATE, state_id)
                )
        except Exception as e:
            logging.debug(e)

    # covid info of  total cases,total Active across india
    def get_covid_info_india(self):
        status = self.fetch(self.config_buff[CASES_ACROSS_INDIA])
        data = {"cases_across":status["country"],
                "Total Confirmed cases": status["cases"],
                "Active": status["active"],
                "Cured/Discharged/Migrated": status["recovered"],
                "Critical": status["critical"],
                "Death": status["deaths"],
                "Tests": status["tests"]
            }
        return data

    def origin(self, act, code=str):
        try:
            if act == INIT:
                self.connect_fetch()
            elif act == STATE_COVID_INFO:
                if self.cache():
                    self.connect_fetch()
                dump = dict()
                for item in self.MASTER_CASES_DICT:
                    if not item in self.ignore_ids:
                        dump[item] = self.MASTER_CASES_DICT[item][str(code)]
                return dump
            elif act == LAST_UPDATE_VACCINE:
                if self.cache():
                    self.connect_fetch()
                dump = dict()
                for item in self.MASTER_VACCINE_DICT:
                    if not item in self.ignore_vacc_ids:
                        inner_dict = self.MASTER_VACCINE_DICT[item][-1]
                        for inner_item in inner_dict:
                            if not inner_item in VACC_ST_DATA:
                                dump[inner_item] = inner_dict[inner_item]
                return dump
            elif act == STATE_COVID_VACCINE_UPDATE:
                if self.cache():
                    self.connect_fetch()
                dump = dict()
                for item in self.MASTER_VACCINE_DICT:
                    if not item in self.ignore_vacc_ids:
                        inner_dict = self.MASTER_VACCINE_DICT[item][-1]
                        for inner_item in inner_dict:
                            if inner_item in VACC_ST_DATA:
                                dump = inner_dict[inner_item][code]
                return dump
        except Exception as e:
            logging.debug(e)
            return None

    def connect_fetch(self):
        try:
            status = self.fetch(self.config_buff[CASES_TIMELINE_STATE])
            if status != None:
                self.MASTER_CASES_DICT = status
            status = self.fetch(self.config_buff[VACCINE_TIMELINE_URL])
            if status != None:
                self.MASTER_VACCINE_DICT = status
        except Exception as e:
            logging.debug(e)
