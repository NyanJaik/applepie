.. default-domain:: py
.. highlight:: python
.. currentmodule:: init

Usage
=====

.. staticmethod:: strip(intext)

   Returns a lowercase version of *intext* without symbols and spaces.

   :param str intext: String containing text.
   :rtype: str



.. staticmethod:: censor(intext)

   Returns a string from *intext* with all offensive words replaced with asterisks.

   :param str intext: String containing text.
   :rtype: str



.. staticmethod:: getnames(intext)

   Returns a list of all names from intext, in chronological order and capitalized.

   :param str intext: String containing names and other text.
   :rtype: list(str)



.. staticmethod:: capitalizenames(intext)

   Returns a string from *intext* with all names capitalized.

   :param str intext: String containing names and other text..
   :rtype: str



.. staticmethod:: gender(intext)

   Returns "male", "female", or "?".

   :param str intext: String containing a single name.
   :rtype: str



.. staticmethod:: yesno(intext)

   Returns True, False, or "?".

   :param str intext: String containing answer to yes or no question.
   :rtype: bool or str
