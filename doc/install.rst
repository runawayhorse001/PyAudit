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

Clone the Repository
++++++++++++++++++++

.. code-block:: bash

	git clone https://github.com/runawayhorse001/PyAudit.git


Install
+++++++

.. code-block:: bash

	cd PyAudit
	pip install -r requirements.txt 
	python setup.py install

Uninstall
+++++++++

.. code-block:: bash

	pip uninstall statspy

Test
++++

.. code-block:: bash

	cd PyAudit/test
	python test1.py


``test1.py``

.. literalinclude:: ../test/test1.py
     :language: python



|rst|	

.. code-block:: python

	[-1.27920153  0.84000173  1.75114469 -0.02731652 -0.56417185 -0.61239996
	 -1.47376967  1.39551562 -0.8559779   0.60139758]

	    --------------------------------------------------------------------------------
	    #       One Sample t-test
	    # data:  ['y']
	    # t = 3.872983346207417, df = 3, p-value = 0.030466291662170977
	    # alternative hypothesis: true mean is not equal to 0.0
	    # 95.0 percent confidence interval:
	    # 0.4457397432391206, 4.554260256760879
	    # mean of x
	    #         2.5
	    --------------------------------------------------------------------------------

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _reStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _LaTex: https://en.wikipedia.org/wiki/LaTeX