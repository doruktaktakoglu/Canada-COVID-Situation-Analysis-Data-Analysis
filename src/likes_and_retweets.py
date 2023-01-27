import pandas as pd
import sys
import json

inputfile = sys.argv[1]

df = pd.read_csv(inputfile, sep='\t')


M_df = df[df['Topic'] =='M']

V_df = df[df['Topic'] =='V']

C_df = df[df['Topic'] =='C']

T_df = df[df['Topic'] =='T']

P_df = df[df['Topic'] =='P']

S_df = df[df['Topic'] =='S']

A_df = df[df['Topic'] =='A']

U_df = df[df['Topic'] =='U']


m_like = 0
v_like = 0
c_like = 0
t_like = 0
p_like = 0
s_like = 0
a_like = 0
u_like = 0

m_retweet = 0
v_retweet = 0
c_retweet = 0
t_retweet = 0
p_retweet = 0
s_retweet = 0
a_retweet = 0
u_retweet = 0

m_count = 0
v_count = 0
c_count = 0
t_count = 0
p_count = 0
s_count = 0
a_count = 0
u_count = 0

m_pos_like = 0
v_pos_like = 0
c_pos_like = 0
t_pos_like = 0
p_pos_like = 0
s_pos_like = 0
a_pos_like = 0
u_pos_like = 0

m_pos_retweet = 0
v_pos_retweet = 0
c_pos_retweet = 0
t_pos_retweet = 0
p_pos_retweet = 0
s_pos_retweet = 0
a_pos_retweet = 0
u_pos_retweet = 0

m_pos_count = 0
v_pos_count = 0
c_pos_count = 0
t_pos_count = 0
p_pos_count = 0
s_pos_count = 0
a_pos_count = 0
u_pos_count = 0

m_neg_like = 0
v_neg_like = 0
c_neg_like = 0
t_neg_like = 0
p_neg_like = 0
s_neg_like = 0
a_neg_like = 0
u_neg_like = 0

m_neg_retweet = 0
v_neg_retweet = 0
c_neg_retweet = 0
t_neg_retweet = 0
p_neg_retweet = 0
s_neg_retweet = 0
a_neg_retweet = 0
u_neg_retweet = 0

m_neg_count = 0
v_neg_count = 0
c_neg_count = 0
t_neg_count = 0
p_neg_count = 0
s_neg_count = 0
a_neg_count = 0
u_neg_count = 0

m_neu_like = 0
v_neu_like = 0
c_neu_like = 0
t_neu_like = 0
p_neu_like = 0
s_neu_like = 0
a_neu_like = 0
u_neu_like = 0

m_neu_retweet = 0
v_neu_retweet = 0
c_neu_retweet = 0
t_neu_retweet = 0
p_neu_retweet = 0
s_neu_retweet = 0
a_neu_retweet = 0
u_neu_retweet = 0

m_neu_count = 0
v_neu_count = 0
c_neu_count = 0
t_neu_count = 0
p_neu_count = 0
s_neu_count = 0
a_neu_count = 0
u_neu_count = 0


for index, row in M_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    m_like += cur_like
    m_retweet += cur_retweet
    m_count += 1
    if (row['sentiment'] == 'positive'):
        m_pos_like += cur_like
        m_pos_retweet += cur_retweet
        m_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        m_neg_like += cur_like
        m_neg_retweet += cur_retweet
        m_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        m_neu_like += cur_like
        m_neu_retweet += cur_retweet
        m_neu_count += 1

for index, row in V_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    v_like += cur_like
    v_retweet += cur_retweet
    v_count += 1
    if (row['sentiment'] == 'positive'):
        v_pos_like += cur_like
        v_pos_retweet += cur_retweet
        v_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        v_neg_like += cur_like
        v_neg_retweet += cur_retweet
        v_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        v_neu_like += cur_like
        v_neu_retweet += cur_retweet
        v_neu_count += 1

for index, row in C_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    c_like += cur_like
    c_retweet += cur_retweet
    c_count += 1
    if (row['sentiment'] == 'positive'):
        c_pos_like += cur_like
        c_pos_retweet += cur_retweet
        c_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        c_neg_like += cur_like
        c_neg_retweet += cur_retweet
        c_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        c_neu_like += cur_like
        c_neu_retweet += cur_retweet
        c_neu_count += 1

for index, row in T_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    t_like += cur_like
    t_retweet += cur_retweet
    t_count += 1
    if (row['sentiment'] == 'positive'):
        t_pos_like += cur_like
        t_pos_retweet += cur_retweet
        t_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        t_neg_like += cur_like
        t_neg_retweet += cur_retweet
        t_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        t_neu_like += cur_like
        t_neu_retweet += cur_retweet
        t_neu_count += 1

for index, row in P_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    p_like += cur_like
    p_retweet += cur_retweet
    p_count += 1
    if (row['sentiment'] == 'positive'):
        p_pos_like += cur_like
        p_pos_retweet += cur_retweet
        p_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        p_neg_like += cur_like
        p_neg_retweet += cur_retweet
        p_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        p_neu_like += cur_like
        p_neu_retweet += cur_retweet
        p_neu_count += 1

for index, row in S_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    s_like += cur_like
    s_retweet += cur_retweet
    s_count += 1
    if (row['sentiment'] == 'positive'):
        s_pos_like += cur_like
        s_pos_retweet += cur_retweet
        s_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        s_neg_like += cur_like
        s_neg_retweet += cur_retweet
        s_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        s_neu_like += cur_like
        s_neu_retweet += cur_retweet
        s_neu_count += 1

for index, row in A_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    a_like += cur_like
    a_retweet += cur_retweet
    a_count += 1
    if (row['sentiment'] == 'positive'):
        a_pos_like += cur_like
        a_pos_retweet += cur_retweet
        a_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        a_neg_like += cur_like
        a_neg_retweet += cur_retweet
        a_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        a_neu_like += cur_like
        a_neu_retweet += cur_retweet
        a_neu_count += 1

for index, row in U_df.iterrows():
    cur_like = row['like_count']
    cur_retweet = row['retweet_count']
    u_like += cur_like
    u_retweet += cur_retweet
    u_count += 1
    if (row['sentiment'] == 'positive'):
        u_pos_like += cur_like
        u_pos_retweet += cur_retweet
        u_pos_count += 1
    elif (row['sentiment'] == 'negative'):
        u_neg_like += cur_like
        u_neg_retweet += cur_retweet
        u_neg_count += 1
    elif (row['sentiment'] == 'neutral'):
        u_neu_like += cur_like
        u_neu_retweet += cur_retweet
        u_neu_count += 1


m_like_ratio = m_like / m_count
v_like_ratio = v_like / v_count
c_like_ratio = c_like / c_count
t_like_ratio = t_like / t_count
p_like_ratio = p_like / p_count
s_like_ratio = s_like / s_count
a_like_ratio = a_like / a_count
u_like_ratio = u_like / u_count

m_retweet_ratio = m_retweet / m_count
v_retweet_ratio = v_retweet / v_count
c_retweet_ratio = c_retweet / c_count
t_retweet_ratio = t_retweet / t_count
p_retweet_ratio = p_retweet / p_count
s_retweet_ratio = s_retweet / s_count
a_retweet_ratio = a_retweet / a_count
u_retweet_ratio = u_retweet / u_count

m_dict = dict()
v_dict = dict()
c_dict = dict()
t_dict = dict()
p_dict = dict()
s_dict = dict()
a_dict = dict()
u_dict = dict()

m_dict['total number of likes'] = m_like
m_dict['total number of tweets'] = m_count
m_dict['total number of retweets'] = m_retweet
m_dict['total number of likes for positive tweets'] = m_pos_like
m_dict['total number of positive tweets'] = m_pos_count
m_dict['total number of positive retweets'] = m_pos_retweet
m_dict['total number of likes for neutral tweets'] = m_neu_like
m_dict['total number of neutral tweets'] = m_neu_count
m_dict['total number of neutral retweets'] = m_neu_retweet
m_dict['total number of likes for negative tweets'] = m_neg_like
m_dict['total number of negative tweets'] = m_neg_count
m_dict['total number of negative retweets'] = m_neg_retweet
if (m_count != 0):
    m_dict['like per tweet'] = m_like_ratio
    m_dict['retweet per tweet'] = m_retweet_ratio
if (m_pos_count != 0):
    m_dict['retweet per positive tweet'] = (m_pos_retweet / m_pos_count)
    m_dict['like per positive tweet'] = (m_pos_like / m_pos_count)
if (m_neg_count != 0):
    m_dict['retweet per negative tweet'] = (m_neg_retweet / m_neg_count)
    m_dict['like per negative tweet'] = (m_neg_like / m_neg_count)
if (m_neu_count != 0):
    m_dict['retweet per neutral tweet'] = (m_neu_retweet / m_neu_count)
    m_dict['like per neutral tweet'] = (m_neu_like / m_neu_count)



v_dict['total number of likes'] = v_like
v_dict['total number of tweets'] = v_count
v_dict['total number of retweets'] = v_retweet
v_dict['total number of likes for positive tweets'] = v_pos_like
v_dict['total number of positive tweets'] = v_pos_count
v_dict['total number of positive retweets'] = v_pos_retweet
v_dict['total number of likes for neutral tweets'] = v_neu_like
v_dict['total number of neutral tweets'] = v_neu_count
v_dict['total number of neutral retweets'] = v_neu_retweet
v_dict['total number of likes for negative tweets'] = v_neg_like
v_dict['total number of negative tweets'] = v_neg_count
v_dict['total number of negative retweets'] = v_neg_retweet
if (v_count != 0):
    v_dict['like per tweet'] = v_like_ratio
    v_dict['retweet per tweet'] = v_retweet_ratio
if (v_pos_count != 0):
    v_dict['retweet per positive tweet'] = (v_pos_retweet / v_pos_count)
    v_dict['like per positive tweet'] = (v_pos_like / v_pos_count)
if (v_neg_count != 0):
    v_dict['retweet per negative tweet'] = (v_neg_retweet / v_neg_count)
    v_dict['like per negative tweet'] = (v_neg_like / v_neg_count)
if (v_neu_count != 0):
    v_dict['retweet per neutral tweet'] = (v_neu_retweet / u_neu_count)
    v_dict['like per neutral tweet'] = (v_neu_like / u_neu_count)



c_dict['total number of likes'] = c_like
c_dict['total number of tweets'] = c_count
c_dict['total number of retweets'] = c_retweet
c_dict['total number of likes for positive tweets'] = c_pos_like
c_dict['total number of positive tweets'] = c_pos_count
c_dict['total number of positive retweets'] = c_pos_retweet
c_dict['total number of likes for neutral tweets'] = c_neu_like
c_dict['total number of neutral tweets'] = c_neu_count
c_dict['total number of neutral retweets'] = c_neu_retweet
c_dict['total number of likes for negative tweets'] = c_neg_like
c_dict['total number of negative tweets'] = c_neg_count
c_dict['total number of negative retweets'] = c_neg_retweet
if (c_count != 0):
    c_dict['like per tweet'] = c_like_ratio
    c_dict['retweet per tweet'] = c_retweet_ratio
if (c_pos_count != 0):
    c_dict['retweet per positive tweet'] = (c_pos_retweet / c_pos_count)
    c_dict['like per positive tweet'] = (c_pos_like / c_pos_count)
if (c_neg_count != 0):
    c_dict['retweet per negative tweet'] = (c_neg_retweet / c_neg_count)
    c_dict['like per negative tweet'] = (c_neg_like / c_neg_count)
if (c_neu_count != 0):
    c_dict['retweet per neutral tweet'] = (c_neu_retweet / c_neu_count)
    c_dict['like per neutral tweet'] = (c_neu_like / c_neu_count)


t_dict['total number of likes'] = t_like
t_dict['total number of tweets'] = t_count
t_dict['total number of retweets'] = t_retweet
t_dict['total number of likes for positive tweets'] = t_pos_like
t_dict['total number of positive tweets'] = t_pos_count
t_dict['total number of positive retweets'] = t_pos_retweet
t_dict['total number of likes for neutral tweets'] = t_neu_like
t_dict['total number of neutral tweets'] = t_neu_count
t_dict['total number of neutral retweets'] = t_neu_retweet
t_dict['total number of likes for negative tweets'] = t_neg_like
t_dict['total number of negative tweets'] = t_neg_count
t_dict['total number of negative retweets'] = t_neg_retweet
if (t_count != 0):
    t_dict['like per tweet'] = t_like_ratio
    t_dict['retweet per tweet'] = t_retweet_ratio
if (t_pos_count != 0):
    t_dict['retweet per positive tweet'] = (t_pos_retweet / t_pos_count)
    t_dict['like per positive tweet'] = (t_pos_like / t_pos_count)
if (t_neg_count != 0):
    t_dict['retweet per negative tweet'] = (t_neg_retweet / t_neg_count)
    t_dict['like per negative tweet'] = (t_neg_like / t_neg_count)
if (t_neu_count != 0):
    t_dict['retweet per neutral tweet'] = (t_neu_retweet / t_neu_count)
    t_dict['like per neutral tweet'] = (t_neu_like / t_neu_count)


p_dict['total number of likes'] = p_like
p_dict['total number of tweets'] = p_count
p_dict['total number of retweets'] = p_retweet
p_dict['total number of likes for positive tweets'] = p_pos_like
p_dict['total number of positive tweets'] = p_pos_count
p_dict['total number of positive retweets'] = p_pos_retweet
p_dict['total number of likes for neutral tweets'] = p_neu_like
p_dict['total number of neutral tweets'] = p_neu_count
p_dict['total number of neutral retweets'] = p_neu_retweet
p_dict['total number of likes for negative tweets'] = p_neg_like
p_dict['total number of negative tweets'] = p_neg_count
p_dict['total number of negative retweets'] = p_neg_retweet
if (p_count != 0):
    p_dict['like per tweet'] = p_like_ratio
    p_dict['retweet per tweet'] = p_retweet_ratio
if (p_pos_count != 0):
    p_dict['retweet per positive tweet'] = (p_pos_retweet / p_pos_count)
    p_dict['like per positive tweet'] = (p_pos_like / p_pos_count)
if (p_neg_count != 0):
    p_dict['retweet per negative tweet'] = (p_neg_retweet / p_neg_count)
    p_dict['like per negative tweet'] = (p_neg_like / p_neg_count)
if (p_neu_count != 0):
    p_dict['retweet per neutral tweet'] = (p_neu_retweet / p_neu_count)
    p_dict['like per neutral tweet'] = (p_neu_like / p_neu_count)

s_dict['total number of likes'] = s_like
s_dict['total number of tweets'] = s_count
s_dict['total number of retweets'] = s_retweet
s_dict['total number of likes for positive tweets'] = s_pos_like
s_dict['total number of positive tweets'] = s_pos_count
s_dict['total number of positive retweets'] = s_pos_retweet
s_dict['total number of likes for neutral tweets'] = s_neu_like
s_dict['total number of neutral tweets'] = s_neu_count
s_dict['total number of neutral retweets'] = s_neu_retweet
s_dict['total number of likes for negative tweets'] = s_neg_like
s_dict['total number of negative tweets'] = s_neg_count
s_dict['total number of negative retweets'] = s_neg_retweet
if (s_count != 0):
    s_dict['like per tweet'] = s_like_ratio
    s_dict['retweet per tweet'] = s_retweet_ratio
if (s_pos_count != 0):
    s_dict['retweet per positive tweet'] = (s_pos_retweet / s_pos_count)
    s_dict['like per positive tweet'] = (s_pos_like / s_pos_count)
if (s_neg_count != 0):
    s_dict['retweet per negative tweet'] = (s_neg_retweet / s_neg_count)
    s_dict['like per negative tweet'] = (s_neg_like / s_neg_count)
if (s_neu_count != 0):
    s_dict['retweet per neutral tweet'] = (s_neu_retweet / s_neu_count)
    s_dict['like per neutral tweet'] = (s_neu_like / s_neu_count)


a_dict['total number of likes'] = a_like
a_dict['total number of tweets'] = a_count
a_dict['total number of retweets'] = a_retweet
a_dict['total number of likes for positive tweets'] = a_pos_like
a_dict['total number of positive tweets'] = a_pos_count
a_dict['total number of positive retweets'] = a_pos_retweet
a_dict['total number of likes for neutral tweets'] = a_neu_like
a_dict['total number of neutral tweets'] = a_neu_count
a_dict['total number of neutral retweets'] = a_neu_retweet
a_dict['total number of likes for negative tweets'] = a_neg_like
a_dict['total number of negative tweets'] = a_neg_count
a_dict['total number of negative retweets'] = a_neg_retweet
if (a_count != 0):
    a_dict['like per tweet'] = a_like_ratio
    a_dict['retweet per tweet'] = a_retweet_ratio
if (a_pos_count != 0):
    a_dict['retweet per positive tweet'] = (a_pos_retweet / a_pos_count)
    a_dict['like per positive tweet'] = (a_pos_like / a_pos_count)
if (a_neg_count != 0):
    a_dict['retweet per negative tweet'] = (a_neg_retweet / a_neg_count)
    a_dict['like per negative tweet'] = (a_neg_like / a_neg_count)
if (a_neu_count != 0):
    a_dict['retweet per neutral tweet'] = (a_neu_retweet / a_neu_count)
    a_dict['like per neutral tweet'] = (a_neu_like / a_neu_count)


u_dict['total number of likes'] = u_like
u_dict['total number of tweets'] = u_count
u_dict['total number of retweets'] = u_retweet
u_dict['total number of likes for positive tweets'] = u_pos_like
u_dict['total number of positive tweets'] = u_pos_count
u_dict['total number of positive retweets'] = u_pos_retweet
u_dict['total number of likes for neutral tweets'] = u_neu_like
u_dict['total number of neutral tweets'] = u_neu_count
u_dict['total number of neutral retweets'] = u_neu_retweet
u_dict['total number of likes for negative tweets'] = u_neg_like
u_dict['total number of negative tweets'] = u_neg_count
u_dict['total number of negative retweets'] = u_neg_retweet

if (u_count != 0):
    u_dict['like per tweet'] = u_like_ratio
    u_dict['retweet per tweet'] = u_retweet_ratio
if (u_pos_count != 0):
    u_dict['retweet per positive tweet'] = (u_pos_retweet / u_pos_count)
    u_dict['like per positive tweet'] = (u_pos_like / u_pos_count)
if (u_neg_count != 0):
    u_dict['retweet per negative tweet'] = (u_neg_retweet / u_neg_count)
    u_dict['like per negative tweet'] = (u_neg_like / u_neg_count)
if (u_neu_count != 0):
    u_dict['retweet per neutral tweet'] = (u_neu_retweet / u_neu_count)
    u_dict['like per neutral tweet'] = (u_neu_like / u_neu_count)

end_product_dict = dict()

end_product_dict['M'] = m_dict
end_product_dict['V'] = v_dict
end_product_dict['C'] = c_dict
end_product_dict['T'] = t_dict
end_product_dict['P'] = p_dict
end_product_dict['S'] = s_dict
end_product_dict['A'] = a_dict
end_product_dict['U'] = u_dict

out_file = open('end_product.json', "w")
json.dump(end_product_dict, out_file, indent = 4)
