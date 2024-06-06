import pickle
from calc_parser import *

# Load compiled parser from file
with open('parser.pickle', 'rb') as f:
    parser = pickle.load(f)

def eval_exp(exp):
    return parser.parse(exp)

print(eval_exp('10^3+400-63'))