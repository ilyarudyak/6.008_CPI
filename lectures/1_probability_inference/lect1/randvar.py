import comp_prob_inference

# approach 1
# prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
#
# W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
# I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}
#
# random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
#
# W = W_mapping[random_outcome]
# I = I_mapping[random_outcome]

# approach2
W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
I_table = {0: 1/2, 1: 1/2}

for i in range(1, 1000):
    W = comp_prob_inference.sample_from_finite_probability_space(W_table)
    I = comp_prob_inference.sample_from_finite_probability_space(I_table)
    if W == 'sunny' and I == 0:
        print("W=" + str(W) + " I=" + str(I))
        break
