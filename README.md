# logica_para_computacao
## Rodar o FLiP-py3
<pre>
	cd FLiP-py3/flip/logic && python -i -m prop_derived_session	
</pre>

### Comentarios na Demonstracao do Flip
<code>
checkp(Text('Testando o flip'), comment)
</code> 

### Criar premissa
<code>
checkp(Impl(j, Impl(j, m)), given)
</code>

### Verificar nomes das regras
<code>
rule_names
</code>

### Verificar regras
<code>
>>> rules()
[('comment', ['m1']),
 ('given', ['m1']),
 ('assume', ['m1']),
 ('top', ['T']),
 ('ai', ['m1', 'm2', 'And(m1,m2)']),
 ('ael', ['And(m1,m2)', 'm2']),
 ('aer', ['And(m1,m2)', 'm1']),
 ('oil', ['m2', 'Or(m1,m2)']),
 ('oir', ['m1', 'Or(m1,m2)']),
 ('contra', ['m1', 'Not(m1)', 'F']),
 ('raa', ['m1', 'F', 'Not(m1)']),
 ('impli', ['m1', 'm2', 'Impl(m1,m2)']),
 ('imple', ['Impl(m1,m2)', 'm1', 'm2']),
 ('assume_case', ['m1']),
 ('ore', ['Or(m1,m2)', 'm1', 'm3', 'm2', 'm3', 'm3']),
 ('fe', ['F', 'm1']),
 ('nne', ['Not(Not(m1))', 'm1']),
 ('mt', ['Impl(m1,m2)', 'Not(m2)', 'Not(m1)']),
 ('nni', ['m1', 'Not(Not(m1))']),
 ('pbc', ['Not(m1)', 'F', 'm1']),
 ('lem', ['Or(m1,Not(m1))']),
 ('copy', ['m1', 'm1'])]
 </code>

### Suposicao
<code>
checkp(j, assume)
</code>

###