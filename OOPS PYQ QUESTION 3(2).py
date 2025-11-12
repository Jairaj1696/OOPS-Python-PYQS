S1={'Amar', 'Amy', 'Aryan', 'Ajay','Beena', 'Brij'}
S2={x for x in S1 if x.startswith('A')}
S3={x for x in S1 if x.startswith('B')}
print(S1)
print(S2)
print(S3)