# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 00:03:44 2016

@author: ilyarudyak
"""

from simpsons_paradox_data import *
import numpy as np
np.set_printoptions(precision=4)

#joint_prob_table[gender_mapping['female'], department_mapping['A'], admission_mapping['admitted']]

joint_prob_gender_admission = joint_prob_table.sum(axis=1)

female_only = joint_prob_gender_admission[gender_mapping['female']]
prob_admission_given_female = female_only / np.sum(female_only)

male_only = joint_prob_gender_admission[gender_mapping['male']]
prob_admission_given_male = male_only / np.sum(male_only)

#prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
#print(prob_admission_given_female_dict)

for label in department_labels:
    admitted_femail = joint_prob_table[gender_mapping['female'], department_mapping[label]]
    admitted_femail_norm = admitted_femail / np.sum(admitted_femail)
    admitted_male = joint_prob_table[gender_mapping['male'], department_mapping[label]]
    admitted_male_norm = admitted_male / np.sum(admitted_male)
    print(str(label) + ": femail " + '{:.3f}'.format(admitted_femail_norm[0]) + " mail " + '{:.3f}'.format(admitted_male_norm[0])) 
    