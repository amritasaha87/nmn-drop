from utils.datetimeutils import *

class ner_process():

    def parseDateNERS(ners, token):
        dates = [d for d in ners if d[-1]=='DATE']
        p_parsed_dates = [(d[0], (d[1], d[2]), d[0]) for d in dates]
        p_normalized_date_idxs = [i for i,d in enumerate(dates)]#[i for (i,d) in dates]
        p_normalized_date_values = [get_date_from_string(d[0]) for d in dates]
        return p_parsed_dates, p_normalized_date_idxs, p_normalized_date_values, None

    def parseNumNERS(ners, token):
        nums = [d for d in ners if d[-1]=='QUANTITY' or d[-1]=='CARDINAL']
        p_parsed_nums = [(d[0], d[1], d[0]) for d in nums]
        p_normalized_nums_idxs = [i for i,d in enumerate(nums)]#[i for (i,d) in nums]
        p_normalized_nums_values = [get_number_from_string(d[0]) for d in nums]
        return p_parsed_nums, p_normalized_nums_idxs, p_normalized_nums_values, None    



 