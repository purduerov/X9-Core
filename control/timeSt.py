�
���Wc           @   s�   d  g Z  d d l Z d d l Z d Z d e j f d �  �  YZ e j d d e �Z e j	 Z	 e j
 e j e � g e	 _ d �  Z d	 �  Z d S(
   t   monotonic_timei����Ni   t   timespecc           B   s&   e  Z d  e j f d e j f g Z RS(   t   tv_sect   tv_nsec(   t   __name__t
   __module__t   ctypest   c_longt   _fields_(    (    (    s,   /home/trotsky/Downloads/TimeStampReturner.pyR      s   s
   librt.so.1t	   use_errnoc          C   s`   t  �  }  t t t j |  � � d k rN t j �  } t | t j | � � � n  |  j	 |  j
 d S(   Ni    g��&�.>(   R   t   clock_gettimet   CLOCK_MONOTONIC_RAWR   t   pointert	   get_errnot   OSErrort   ost   strerrorR   R   (   t   tt   errno_(    (    s,   /home/trotsky/Downloads/TimeStampReturner.pyR       s
    	c         C   s   | |  S(   N(    (   t   prevTimet   newTime(    (    s,   /home/trotsky/Downloads/TimeStampReturner.pyt   TimeStep   s    (   t   ll__R   R   R   t	   StructureR   t   CDLLt   Truet   librtR
   t   c_intt   POINTERt   argtypesR    R   (    (    (    s,   /home/trotsky/Downloads/TimeStampReturner.pyt   <module>   s   			