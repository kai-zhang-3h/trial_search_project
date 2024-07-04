from trial_search_crawler.utils.schema import table_info, table_insert, gender_mapping, prefecture_mapping
from datetime import date

class Wrapper:

    no_exception = True
    e = ""

    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self, t_name):
        self.cursor.execute('DROP TABLE IF EXISTS ' + t_name)
        fields_info = table_insert[t_name]["fields_info"]
        fields_string = ", ".join(list(map(lambda e: e[0] + " " + e[1], list(fields_info.items()))))
        create_query = "CREATE Table " + t_name + "(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " + fields_string + ")DEFAULT CHARACTER SET=utf8"
        self.cursor.execute(create_query)
    
    # Function that transform the data in adaptor into the form of required output
    def preprocess(self, adapter):
        res = {}
        jrctid = adapter["jrctid"]
        today = str(date.today())
        for k in table_insert.keys():
            res[k] = {}
            res[k]["jrctid"] = jrctid
            res[k]["date_signup"] = today
            res[k]["date_update"] = today
            for key in adapter[k].keys():
                res[k][key] = adapter[k][key]

        res["t_basic"] = modify_t_basic(res["t_basic"])
        res["t_summary"] = modify_t_summmary(res["t_summary"])
        res["t_qualification"] = modify_t_qualification(res["t_qualification"])
        res["t_committee"] = modify_t_committee(res["t_committee"])
        res["t_cancel"] = modify_t_cancel(res["t_cancel"])
        res["t_end"] = modify_t_end(res["t_end"])

        return res
    
    def insert_record(self, t_name, jrctdict):
        val_list = list(jrctdict[t_name].values())
        keys_list = list(table_insert[t_name]["fields_info"].keys())
        fields_key_string = " (" + ", ".join(keys_list) + ")"
        insert_query = "INSERT INTO " + t_name + fields_key_string + " VALUES " + "(" + '%s, ' * (len(val_list) - 1) + '%s' + ")"
        try:
            self.cursor.execute(insert_query, tuple(val_list))
        except Exception as e:
            self.e = str(e)
            self.no_exception = False
    
    def extract_id(response):
        return response.xpath('.//table')[0].xpath('.//td')[0].xpath('.//text()').get()
    
    def extract_table(response, t_name):
        fields = list(table_info[t_name]["fields_info"].keys())
        cells = list(map(lambda x:x.xpath('.//text()').get(), response.xpath('.//table')[table_info[t_name]["num"]].xpath('.//td')))
        return dict(zip(fields, cells))

def modify_t_basic(t_dict):
    #t_basic： delete repeated key
    t_dict.pop("jrctidrepeat")
    t_dict.pop("date_signup_old")
    t_dict.pop("date_update_old")

    t_dict["date_start"] = format_date(t_dict["date_start"])
    t_dict["date_end"] = format_date(t_dict["date_end"])
    t_dict["date_enroll"] = format_date(t_dict["date_enroll"])

    return t_dict

def modify_t_summmary(t_dict):
    #t_summary: utilize prefecture mapping
    if (t_dict["prefecture_jp"]) is None:
        return t_dict
    t_dict["prefecture_jp"] = prefecture_mapping[t_dict["prefecture_jp"]]
    t_dict["prefecture_en"] = t_dict["prefecture_jp"]

    return t_dict

def modify_t_qualification(t_dict):
    #t_qualification: utilize gender mapping and convert age into integer with day as unit
    if (t_dict["gender_jp"]) is not None:
        t_dict["gender_jp"] = gender_mapping[t_dict["gender_jp"]]
        t_dict["gender_en"] = t_dict["gender_jp"]
    t_dict["age_min_jp"] = format_age(t_dict["age_min_jp"])
    t_dict["age_min_en"] = t_dict["age_min_jp"]
    t_dict["age_max_jp"] = format_age(t_dict["age_max_jp"])
    t_dict["age_max_en"] = t_dict["age_max_jp"]
    return t_dict

def modify_t_committee(t_dict):
    #t_committee: change format of date
    t_dict["date_approval"] = format_date(t_dict["date_approval"])
    return t_dict

def modify_t_cancel(t_dict):
    #t_cancel: change format of date
    t_dict["date_cancel_notification"] = format_date(t_dict["date_cancel_notification"])
    t_dict["date_cancel"] = format_date(t_dict["date_cancel"])
    
    return t_dict

def modify_t_end(t_dict):
    #t_end: change the format of date
    t_dict["date_end_notification"] = format_date(t_dict["date_end_notification"])
    t_dict["date_end"] = format_date(t_dict["date_end"])
    t_dict["date_publication"] = format_date_sequence(t_dict["date_publication"])
    t_dict["date_initial_publication"] = format_date(t_dict["date_initial_publication"])

    return t_dict

# Deal with date in the form of xxxx年xx月xx日
def format_date(s):
    if s is None:
        return s
    return s.replace("年", "-").replace("月", "-").replace("日", "")

# Deal with date in the form of mm/dd/yy
def format_date_sequence(s):
    if s is None:
        return s
    lst = s.split('/')
    lst.insert(0, lst.pop())
    return '-'.join(lst)

# Parse age. All converted to integer with day as base unit
def format_age(s):
    if s is None:
        return s
    if "週" in s:
        return int(s.split("週")[0])*7
    elif "月" in s:
        return int(s.split("月")[0])*30
    else:
        return int(s.split("歳")[0])*365
