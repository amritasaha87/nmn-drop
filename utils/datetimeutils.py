import datefinder
from word2number import w2n
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
import numpy

nlp = English()
tokenizer = nlp.Defaults.create_tokenizer(nlp)

words_to_ordinal = {"first":1, "second":2, "third":3, "fourth":4, "fifth":5, "sixth":6, "seventh":7, "eighth":8, "ninth":9, "tenth":10, "eleventh":11, "1st":1, "2nd":2, "3rd":3, "4th":4, "5th":5, "6th":6, "7th":7, "8th":8, "9th":9, "10th":10, "11th":11, "12th":12}
words_to_frac = {"full":1, "half":0.5, "halves":0.5, "quarter":0.25, "quarters":0.25}

def extract_custom_date(s):
    s = s.lower()
    print ('in extract custom date ', s)
    date = None
    if 'week' in s:
        nums = get_number_from_string(s)
        if nums==-1:
            nums=1
        day = nums*7
        if day > 31:
            day = int(day%31)
            month = int(day/31)
        else:
            month = 1    
        year = 0
        date = (day, month, year)
    if 'month' in s:
        nums = get_number_from_string(s)
        if nums==-1:
            nums=1
        month = nums
        if month > 12:
            month = int(month%12)
            year = int(month/12)
        else:
            year = 0       
        date = (1, month, year)
    if 'year' in s:
        year = get_number_from_string(s)
        if year==-1:
            year=1
        date = (1, 1, year)
    return date                



def extract_custom_numbers(s):
    ordinal_numbers = []
    for w in s.split(' '):
        if w in words_to_ordinal:
            ordinal_numbers.append(words_to_ordinal[w])
    frac_numbers = []
    for w in s.split(' '):
        if w in words_to_frac:
            frac_numbers.append(words_to_frac[w])
    if len(frac_numbers)>0 or len(ordinal_numbers)>0:        
        result = numpy.prod(ordinal_numbers)*numpy.prod(frac_numbers)
        date = (1, int(12*result), 0)
        print ('found custom DATE for', s, '->', date)
    else:
        date = extract_custom_date(s)
        if not date:
            print ('found no DATE for ', s) 
            date = (-1, -1, -1)    
        else:
            print ('found custom DATE for ', s, '->', date)    
    return date

def get_date_from_string(s):
        dates = []
        try:
            for dt in datefinder.find_dates(s):
                dates.append((dt.date().day, dt.date().month, dt.date().year))
        except:
            dates = []        
        if len(dates)==0:
            dates.append(extract_custom_numbers(s))
        return dates[0]    

def get_number_from_string(s):
        s = s.replace(',','')
        nums = []
        for token in tokenizer(s):
            try:
                nums.append(w2n.word_to_num(str(token)))
            except:
                continue    
        if len(nums)>0:
            nums = nums[0]
        else:
            print ('found no NUM for ', s)
            nums = -1    
        return nums    