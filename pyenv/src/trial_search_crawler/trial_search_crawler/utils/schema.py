table_info = {
    "t_basic": {"num" : 0,
                "name" : "t_basic",
                "fields_info": {"jrctidrepeat": "VARCHAR(255) NOT NULL", "title_r_jp": "TEXT", "title_r_en": "TEXT", "title_p_jp": "TEXT","title_p_en": "TEXT", "status_jp": "VARCHAR(255)",
                                "status_en": "VARCHAR(255)", "date_signup_old": "VARCHAR(255)", "date_update_old": "VARCHAR(255)", "date_start": "VARCHAR(255)", "date_end": "VARCHAR(255)", "date_enroll": "VARCHAR(255)"}
               },
    "t_summary": {"num" : 1,
                "name" : "t_summary",
                "fields_info": {"region_jp": "TEXT", "region_en": "TEXT", "prefecture_jp": "TEXT", "prefecture_en": "VARCHAR(255)","sample_size": "VARCHAR(255)", "condition_jp": "TEXT",
                                "condition_en": "TEXT", "study_type_jp": "VARCHAR(255)", "study_type_en": "VARCHAR(255)", "study_design_jp": "TEXT", "study_design_en": "TEXT", "random_jp": "TEXT",
                                "random_en": "TEXT", "intervention1_jp": "TEXT", "intervention1_en": "TEXT", "primary_outcomes_jp": "TEXT", "primary_outcomes_en": "TEXT", 
                                "secondary_outcomes_jp": "TEXT", "secondary_outcomes_en": "TEXT"}
               },
    "t_qualification": {"num" : 2,
                "name" : "t_qualification",
                "fields_info": {"age_min_jp": "TEXT", "age_min_en": "TEXT", "age_max_jp": "TEXT", "age_max_en": "TEXT","gender_jp": "VARCHAR(255)", "gender_en": "VARCHAR(255)",
                                "include_criteria_jp": "TEXT", "include_criteria_en": "TEXT", "exclude_criteria_jp": "TEXT", "exclude_criteria_en": "TEXT"}
               },
    "t_researcher": {"num" : 3,
                "name" : "t_researcher",
                "fields_info": {"lead_jp": "TEXT", "lead_en": "TEXT", "org_jp": "TEXT", "org_en": "TEXT","div_jp": "TEXT", "div_en": "TEXT",
                                "address_r_jp": "TEXT", "address_r_en": "TEXT", "tel_r_jp": "TEXT", "tel_r_en": "TEXT","affiliation_jp": "TEXT", 
                                "affiliation_en": "TEXT", "funding_src_jp": "TEXT", "funding_src_en": "TEXT", "coop_src_jp": "TEXT", 
                                "coop_src_en": "TEXT", "researcher_reception_id_jp": "VARCHAR(255)", "researcher_reception_id_en": "TEXT"}
               },
    "t_inquiry": {"num" : 4,
                "name" : "t_inquiry",
                "fields_info": {"address_i_jp": "TEXT", "address_i_en": "TEXT", "tel_i_jp": "VARCHAR(255)", "tel_i_en": "VARCHAR(255)", "homepage_jp": "TEXT", 
                                "homepage_en": "TEXT", "email_i_jp": "TEXT", "email_i_en": "TEXT","poc_jp": "VARCHAR(255)", "poc_en": "TEXT"}
               },
    "t_committee": {"num" : 5,
                "name" : "t_committee",
                "fields_info": {"committee_jp": "TEXT", "committee_en": "TEXT", "committee_num": "TEXT", "address_c_jp": "TEXT", "address_c_en": "TEXT", 
                                "tel_c": "VARCHAR(255)", "email_c": "TEXT", "exam_reception_id": "TEXT","exam_res": "VARCHAR(255)", "date_approval": "VARCHAR(255)"}
               },
    "t_cancel": {"num" : 6,
                "name" : "t_cancel",
                "fields_info": {"date_cancel_notification": "TEXT", "date_cancel": "TEXT", "reason_cancel": "TEXT"}
               },
    "t_end": {"num" : 7,
                "name" : "t_end",
                "fields_info": {"date_end_notification": "VARCHAR(255)", "date_end": "VARCHAR(255)", "num_cases": "VARCHAR(255)", "participant_flow": "TEXT", "participant_background": "TEXT",
                                "disease_status_summary": "TEXT", "data_analysic_res": "TEXT", "date_publication": "VARCHAR(255)", "end_summary": "TEXT", "research_plan_url": "TEXT",
                                "date_initial_publication": "VARCHAR(255)", "publication_url": "TEXT"}
               },
    "t_ipd": {"num" : 8,
                "name" : "t_ipd",
                "fields_info": {"ipd_share_plan": "TEXT", "ipd_share_plan_explanation": "TEXT"}
               }
}

table_insert = {
    "t_basic": {"num" : 0,
                "name" : "t_basic",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "title_r_jp": "TEXT", "title_r_en": "TEXT", "title_p_jp": "TEXT","title_p_en": "TEXT", "status_jp": "VARCHAR(255)",
                                "status_en": "VARCHAR(255)", "date_start": "DATE", "date_end": "DATE", "date_enroll": "DATE"}
               },
    "t_summary": {"num" : 1,
                "name" : "t_summary",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "region_jp": "TEXT", "region_en": "TEXT", "prefecture_jp": "INT", "prefecture_en": "INT","sample_size": "INT", "condition_jp": "TEXT",
                                "condition_en": "TEXT", "study_type_jp": "VARCHAR(255)", "study_type_en": "VARCHAR(255)", "study_design_jp": "TEXT", "study_design_en": "TEXT", "random_jp": "TEXT",
                                "random_en": "TEXT", "intervention1_jp": "TEXT", "intervention1_en": "TEXT", "primary_outcomes_jp": "TEXT", "primary_outcomes_en": "TEXT", 
                                "secondary_outcomes_jp": "TEXT", "secondary_outcomes_en": "TEXT"}
               },
    "t_qualification": {"num" : 2,
                "name" : "t_qualification",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "age_min_jp": "INT", "age_min_en": "INT", "age_max_jp": "INT", "age_max_en": "INT","gender_jp": "INT", "gender_en": "INT",
                                "include_criteria_jp": "TEXT", "include_criteria_en": "TEXT", "exclude_criteria_jp": "TEXT", "exclude_criteria_en": "TEXT"}
               },
    "t_researcher": {"num" : 3,
                "name" : "t_researcher",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "lead_jp": "TEXT", "lead_en": "TEXT", "org_jp": "TEXT", "org_en": "TEXT","div_jp": "TEXT", "div_en": "TEXT",
                                "address_r_jp": "TEXT", "address_r_en": "TEXT", "tel_r_jp": "TEXT", "tel_r_en": "TEXT","affiliation_jp": "TEXT", 
                                "affiliation_en": "TEXT", "funding_src_jp": "TEXT", "funding_src_en": "TEXT", "coop_src_jp": "TEXT", 
                                "coop_src_en": "TEXT", "researcher_reception_id_jp": "VARCHAR(255)", "researcher_reception_id_en": "TEXT"}
               },
    "t_inquiry": {"num" : 4,
                "name" : "t_inquiry",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "address_i_jp": "TEXT", "address_i_en": "TEXT", "tel_i_jp": "TEXT", "tel_i_en": "TEXT", "homepage_jp": "TEXT", 
                                "homepage_en": "TEXT", "email_i_jp": "TEXT", "email_i_en": "TEXT","poc_jp": "TEXT", "poc_en": "TEXT"}
               },
    "t_committee": {"num" : 5,
                "name" : "t_committee",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "committee_jp": "TEXT", "committee_en": "TEXT", "committee_num": "TEXT", "address_c_jp": "TEXT", "address_c_en": "TEXT", 
                                "tel_c": "TEXT", "email_c": "TEXT", "exam_reception_id": "TEXT","exam_res": "VARCHAR(255)", "date_approval": "DATE"}
               },
    "t_cancel": {"num" : 6,
                "name" : "t_cancel",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "date_cancel_notification": "DATE", "date_cancel": "DATE", "reason_cancel": "TEXT"}
               },
    "t_end": {"num" : 7,
                "name" : "t_end",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "date_end_notification": "DATE", "date_end": "DATE", "num_cases": "INT", "participant_flow": "TEXT", "participant_background": "TEXT",
                                "disease_status_summary": "TEXT", "data_analysic_res": "TEXT", "date_publication": "DATE", "end_summary": "TEXT", "research_plan_url": "TEXT",
                                "date_initial_publication": "DATE", "publication_url": "TEXT"}
               },
    "t_ipd": {"num" : 8,
                "name" : "t_ipd",
                "fields_info": {"jrctid": "VARCHAR(255) NOT NULL", "date_signup": "DATE", "date_update": "DATE", "ipd_share_plan": "TEXT", "ipd_share_plan_explanation": "TEXT"}
               }
}

gender_mapping = {"男性":1, "Male":1, "女性":2, "Female":2, "男女両方":3, "Both":3}

prefecture_mapping = {"北海道":1, "Hokkaido":1, "青森県":2, "Aomori":2, "岩手県": 3, "Iwate":3,
                      "宮城県":4, "Miyagi":4, "秋田県":5, "Akita":5, "山形県":6, "Yamagata":6,
                      "福島県":7, "Fukushima":7, "茨城県":8, "Ibaraki":8, "栃木県":9, "Tochigi":9,
                      "群馬県":10, "Gunma":10, "埼玉県":11, "Saitama":11, "千葉県":12, "Chiba":12,
                      "東京都":13, "Tokyo":13, "神奈川県":14, "Kanagawa":14, "新潟県":15, "Niigata":15,
                      "富山県":16, "Toyama":16, "石川県":17, "Ishikawa":17, "福井県":18, "Fukui":18,
                      "山梨県":19, "Yamanashi":19, "長野県":20, "Nagano":20, "岐阜県":21, "Gifu":21,
                      "静岡県":22, "Shizuoka":22, "愛知県":23, "Aichi":23, "三重県":24, "Mie":24,
                      "滋賀県":25, "Shiga":25, "京都府":26, "Kyoto":26, "大阪府":27, "Osaka":27,
                      "兵庫県":28, "Hyogo":28, "奈良県":29, "Nara":29, "和歌山県":30, "Wakayama":30,
                      "鳥取県":31, "Tottori":31, "島根県":32, "Shimane":32, "岡山県":33, "Okayama":33,
                      "広島県":34, "Hiroshima":34, "山口県":35, "Yamaguchi":35, "徳島県":36, "Tokushima":36,
                      "香川県":37, "Kagawa":37, "愛媛県":38, "Ehime":38, "高知県":39, "Kochi":39,
                      "福岡県":40, "Fukuoka":40, "佐賀県":41, "Saga":41, "長崎県":42, "Nagasaki":42,
                      "熊本県":43, "Kumamoto":43, "大分県": 44, "Oita":44, "宮崎県":45, "Miyazaki":45,
                      "鹿児島県":46, "Kagoshima":46, "沖縄県":47, "Okinawa":47}