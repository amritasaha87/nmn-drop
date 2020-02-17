from typing import List, Dict


logicalform2qtype: Dict[str, str] = {'(find_passageSpanAnswer (compare_date_lesser_than find_PassageAttention find_PassageAttention))': 'date_comparison',
                                     '(find_passageSpanAnswer (compare_date_greater_than find_PassageAttention find_PassageAttention))': 'date_comparison',
                                     '(find_passageSpanAnswer (compare_num_lesser_than find_PassageAttention find_PassageAttention))': 'number_comparison',
                                     '(find_passageSpanAnswer (compare_num_greater_than find_PassageAttention find_PassageAttention))': 'number_comparison',
                                     '(find_PassageNumber find_PassageAttention)': 'num_find_qtype',
                                     '(find_PassageNumber (filter_PassageAttention find_PassageAttention))': 'num_filterfind_qtype',
                                     '(find_PassageNumber (minNumPattn find_PassageAttention))': 'min_find_qtype',
                                     '(find_PassageNumber (minNumPattn (filter_PassageAttention find_PassageAttention)))': 'min_filterfind_qtype',
                                     '(find_PassageNumber (maxNumPattn find_PassageAttention))': 'max_find_qtype',
                                     '(find_PassageNumber (maxNumPattn (filter_PassageAttention find_PassageAttention)))': 'max_filterfind_qtype',
                                     '(passageAttn2Count find_PassageAttention)': 'count_find_qtype',
                                     '(passageAttn2Count (filter_PassageAttention find_PassageAttention))': 'count_filterfind_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention find_PassageAttention))': 'relocate_find_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention (filter_PassageAttention find_PassageAttention)))': 'relocate_filterfind_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention (maxNumPattn find_PassageAttention)))': 'relocate_maxfind_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention (maxNumPattn (filter_PassageAttention find_PassageAttention))))': 'relocate_maxfilterfind_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention (minNumPattn find_PassageAttention)))': 'relocate_minfind_qtype',
                                     '(find_passageSpanAnswer (relocate_PassageAttention (minNumPattn (filter_PassageAttention find_PassageAttention))))': 'relocate_minfilterfind_qtype',
                                     '(year_difference_single_event find_PassageAttention)': 'yeardiff_find_qtype',
                                     '(year_difference find_PassageAttention find_PassageAttention)': 'yeardiff_find2_qtype'}


qtype2logicalforms: Dict[str, List[str]] = {'date_comparison': ['(find_passageSpanAnswer (compare_date_lesser_than find_PassageAttention find_PassageAttention))',
                                                                '(find_passageSpanAnswer (compare_date_greater_than find_PassageAttention find_PassageAttention))'],
                                            'number_comparison': ['(find_passageSpanAnswer (compare_num_lesser_than find_PassageAttention find_PassageAttention))',
                                                                  '(find_passageSpanAnswer (compare_num_greater_than find_PassageAttention find_PassageAttention))'],
                                            'num_find_qtype': ['(find_PassageNumber find_PassageAttention)'],
                                            'num_filterfind_qtype': ['(find_PassageNumber (filter_PassageAttention find_PassageAttention))'],
                                            'min_find_qtype': ['(find_PassageNumber (minNumPattn find_PassageAttention))'],
                                            'min_filterfind_qtype': ['(find_PassageNumber (minNumPattn (filter_PassageAttention find_PassageAttention)))'],
                                            'max_find_qtype': ['(find_PassageNumber (maxNumPattn find_PassageAttention))'],
                                            'max_filterfind_qtype': ['(find_PassageNumber (maxNumPattn (filter_PassageAttention find_PassageAttention)))'],
                                            'count_find_qtype': ['(passageAttn2Count find_PassageAttention)'],
                                            'count_filterfind_qtype': ['(passageAttn2Count (filter_PassageAttention find_PassageAttention))'],
                                            'relocate_find_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention find_PassageAttention))'],
                                            'relocate_filterfind_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention (filter_PassageAttention find_PassageAttention)))'],
                                            'relocate_maxfind_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention (maxNumPattn find_PassageAttention)))'],
                                            'relocate_maxfilterfind_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention (maxNumPattn (filter_PassageAttention find_PassageAttention))))'],
                                            'relocate_minfind_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention (minNumPattn find_PassageAttention)))'],
                                            'relocate_minfilterfind_qtype': ['(find_passageSpanAnswer (relocate_PassageAttention (minNumPattn (filter_PassageAttention find_PassageAttention))))'],
                                            'yeardiff_find_qtype': ['(year_difference_single_event find_PassageAttention)'],
                                            'yeardiff_find2_qtype': ['(year_difference find_PassageAttention find_PassageAttention)']}
