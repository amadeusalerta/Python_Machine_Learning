class humans:
          boy=170;
          def running(self,b):
              return b+10;
ali = humans()
print(ali.boy)
print(ali.running(90))

#Eksik Veriler


imputer=SIT(missing_values=nmpy.nan,strategy='mean')

yaslar=veriler.iloc[:,1:4].values
print(yaslar)
imputer=imputer.fit(yaslar[:,1:4])
yaslar[:,1:4]=imputer.transform(yaslar[:,1:4])
print(yaslar)

countries=veriler.iloc[:,0:1].values
print(countries)

label_encoder_01=prp.LabelEncoder()
countries[:,0]=label_encoder_01.fit_transform(veriler.iloc[:,0])
print(countries)

one_hat_encoder_01=prp.OneHotEncoder()
countries=one_hat_encoder_01.fit_transform(countries).toarray()
print(countries)

result= pnd.DataFrame(data=countries,index=range(22),columns=['fr','tr','us'])
print(result)

result_02=pnd.DataFrame(data=yaslar,index=range(22),columns=['boy','kilo','yas'])
print(result_02)

genders=veriler.iloc[:,-1].values
print(genders)

result_03=pnd.DataFrame(data=genders,index=range(22),columns=['cinsiyet'])
print(result_03)
synchron_01=pnd.concat([result,result_02],axis=1)
print(synchron_01)
synchron_02=pnd.concat([synchron_01,result_03],axis=1)
print(synchron_02)