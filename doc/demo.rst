.. _demo:

=====
Demos 
=====
.. |eg| replace:: For example:


This is a usage of :func:`statspy.basics.rnorm`:


|eg|

>>> from PyAudit.basics import missing_rate, zero_rate, dtypes_class
>>> df = pd.read_csv('Heart.csv', dtype={'Sex': bool})
>>> (num_fields, cat_fields, bool_fields, data_types, ty) = dtypes_class(df)
['Age', 'RestBP', 'Chol', 'Fbs', 'RestECG', 'MaxHR', 'ExAng', 'Oldpeak', 'Slope', 'Ca']
['ChestPain', 'Thal', 'AHD']
['Sex']
      feature   dtypes
0         Age    int64
1         Sex     bool
2   ChestPain   object
3      RestBP    int64
4        Chol    int64
5         Fbs    int64
6     RestECG    int64
7       MaxHR    int64
8       ExAng    int64
9     Oldpeak  float64
10      Slope    int64
11         Ca  float64
12       Thal   object
13        AHD   object
      feature   dtypes     class
0         Age    int64   numeric
1         Sex     bool      bool
2   ChestPain   object  category
3      RestBP    int64   numeric
4        Chol    int64   numeric
5         Fbs    int64   numeric
6     RestECG    int64   numeric
7       MaxHR    int64   numeric
8       ExAng    int64   numeric
9     Oldpeak  float64   numeric
10      Slope    int64   numeric
11         Ca  float64   numeric
12       Thal   object  category
13        AHD   object  category




.. code-block:: bash

	       .,,.
	     ,;;*;;;;,
	    .-'``;-');;.
	   /'  .-.  /*;;
	 .'    \d    \;;               .;;;,
	/ o      `    \;    ,__.     ,;*;;;*;,
	\__, _.__,'   \_.-') __)--.;;;;;*;;;;,
	 `""`;;;\       /-')_) __)  `\' ';;;;;;
	    ;*;;;        -') `)_)  |\ |  ;;;;*;
	    ;;;;|        `---`    O | | ;;*;;;
	    *;*;\|                 O  / ;;;;;*
	   ;;;;;/|    .-------\      / ;*;;;;;
	  ;;;*;/ \    |        '.   (`. ;;;*;;;
	  ;;;;;'. ;   |          )   \ | ;;;;;;
	  ,;*;;;;\/   |.        /   /` | ';;;*;
	   ;;;;;;/    |/       /   /__/   ';;;
	   '*wf*/     |       /    |      ;*;
	        `""""`        `""""`     ;'