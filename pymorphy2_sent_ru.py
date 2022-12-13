import streamlit as st
import pymorphy2 as pm
#import pymorphy2_dicts_ru as ru


morph = pm.MorphAnalyzer()
st.title('Введите предложение для разбора')
text=st.text_input('нажмите ENTER для ввода.')

st.header("Выбор частей речи в Вашем предложении:")
st.write(text)

text_clean=re.sub(r'[.,"\'-?:!;]', '', text)
li=list(text_clean.split(" "))

option=st.selectbox("Какую часть речи Вы хотите скрыть в тексте? (по умолчанию- существительные)", ['существительные', 'прилагательные', 'местоимения', 'глаголы', 'причастия', 'деепричастия', 'числительные', 'наречия', 'предикативы', 'предлоги', 'союзы', 'частицы', 'междометия'])
choice=[]
if option=='существительные':
    choice=['NOUN']
elif option=='прилагательные':
    choice=['ADJF', 'ADJS', 'COMP']
elif option=='местоимения':
    choice=['NPRO']
elif option=='глаголы':
    choice=['VERB', 'INFN']
elif option=='причастия':
     choice=['PRTF', 'PRTS']   
elif option=='деепричастия':
    choice=['GRND']
elif option=='числительные':
    choice=['NUMR']
elif option=='наречия':
    choice=['ADVB']
elif option=='предикативы':
    choice=['PRED']
elif option=='предлоги':
    choice=['PREP']
elif option=='союзы':
    choice=['CONJ']
elif option=='частицы':
     choice=['PRCL']
elif option=='междометия':
    choice=['INTJ']       
else:
    choice=['NOUN']
text_new=''
for i,j in enumerate(li):
    #print(i,j)
    if morph.parse(li[i])[0].tag.POS in choice:
        text_new+='___________ '
    else:    
        text_new+= ' '+ j + ' '
#print(text_new)
st.markdown(text_new)
