import streamlit as st

def calculate_emi(p,n,r) :
  emi = p * (r / 100) * (((1 + (r/100))** n) / (((1 + r/100) ** n) - 1))
  return round(emi, 3)

def calculate_outstanding_emi(p, n, r, m) :
  numerator = (p * ((1 + r/100)**n) - (1 + r/100) **m)
  denominator = ((1 + r/100) **n - 1)	
  balance = numerator/denominator
  return round(balance, 3)

st.title("EMI Calculator App")  

principal = st.slider('Principal', 10000, 10000000)
tenure = st.slider('Tenure in years', 1, 30)
roi = st.slider('Rate of interest', 1.00, 15.00)
m = st.slider('Period after which the Outstanding Loan Balance is calculated(in months)',1, (tenure * 12))

n = tenure * 12
r = roi / 12

if st.button('Calculate EMI'):
  calculated_emi = calculate_emi(principal, n, r)
  st.write('If the Principal Amount borrowed is ', principal, 'for the tenure of ', n, 'months with Rate of interest as ', r, 'percent per annum then the Emi will be ', calculated_emi)
if st.button('Calculate Outstanding Loan Balance')  :
  loan = calculate_outstanding_emi(principal, n, r, m)
  st.write('Outstanding Balance Amount is ', loan)