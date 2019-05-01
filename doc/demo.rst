.. _demo:

==============
Auditing Demos 
==============

.. |eg| replace:: For example:

.. |re| replace:: Result:


This is a demo to show how to aduit ``pd.DataFrame`` using ``PyAudit``: 


|eg|

.. literalinclude:: ../test/demo.py
     :language: python


|re|

.. code-block:: bash

	   Age    Sex     ChestPain  RestBP  Chol  ...  Oldpeak  Slope   Ca        Thal  AHD
	0   63   True       typical     145   233  ...      2.3      3  0.0       fixed   No
	1   67   True  asymptomatic     160   286  ...      1.5      2  3.0      normal  Yes
	2   67   True  asymptomatic     120   229  ...      2.6      2  2.0  reversable  Yes
	3   37   True    nonanginal     130   250  ...      3.5      3  0.0      normal   No
	4   41  False    nontypical     130   204  ...      1.4      1  0.0      normal   No

and 


  .. figure:: images/output.png
    :align: center

  .. figure:: images/results.png
    :align: center    


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