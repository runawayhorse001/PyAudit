.. _install:

==============
How to Install
==============

.. |rst| replace:: ``Results``:
..
	.. admonition:: Chinese proverb

	   If you only know yourself, but not your opponent, you may win or may lose.
	   If you know neither yourself nor your enemy, you will always endanger yourself. 
	   – idiom, from Sunzi’s Art of War

Install with ``pip``
++++++++++++++++++++

You can install the ``PyAudit`` from [PyPI](https://pypi.org/project/PyAudit):

.. code-block:: bash

    pip install PyAudit


Install from Repo
+++++++++++++++++


Clone the Repository
--------------------

.. code-block:: bash

	git clone https://github.com/runawayhorse001/PyAudit.git


Install
-------

.. code-block:: bash

	cd PyAudit
	pip install -r requirements.txt 
	python setup.py install

Uninstall
---------

.. code-block:: bash

	pip uninstall statspy

Test
----

.. code-block:: bash

	cd PyAudit/test
	python test.py


``test.py``

.. literalinclude:: ../test/test.py
     :language: python



|rst|	

.. code-block:: bash

	  feature  missing_rate
	0       A          0.25
	1       B          0.00
	2       C          0.25
	  feature  zero_rate
	0       A   0.333333
	1       B   0.750000
	2       C   0.000000
	  feature  feature_variance
	0       A               1.0
	1       B               0.5
	2       C               1.0
	   Age    Sex     ChestPain  RestBP  Chol  ...  Oldpeak  Slope   Ca        Thal  AHD
	0   63   True       typical     145   233  ...      2.3      3  0.0       fixed   No
	1   67   True  asymptomatic     160   286  ...      1.5      2  3.0      normal  Yes
	2   67   True  asymptomatic     120   229  ...      2.6      2  2.0  reversable  Yes
	3   37   True    nonanginal     130   250  ...      3.5      3  0.0      normal   No
	4   41  False    nontypical     130   204  ...      1.4      1  0.0      normal   No

	[5 rows x 14 columns]
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
	      feature  missing_rate
	0         Age      0.000000
	1         Sex      0.000000
	2   ChestPain      0.000000
	3      RestBP      0.000000
	4        Chol      0.000000
	5         Fbs      0.000000
	6     RestECG      0.000000
	7       MaxHR      0.000000
	8       ExAng      0.000000
	9     Oldpeak      0.000000
	10      Slope      0.000000
	11         Ca      0.013201
	12       Thal      0.006601
	13        AHD      0.000000

	Process finished with exit code 0

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _LaTex: https://en.wikipedia.org/wiki/LaTeX