---
title: 'Chapter 1: Beam me up Scotty!'
description:
  'This chapter will be all about beams'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introduction" type="slides,video">

<slides source="chapter1_01_introduction" start="0:09" end="4:30">
</slides>
This chapter will teach you about many cool things and introduce you to the
  most important concepts of the course.
</exercise>

<exercise id="2" title="Quiz 1">

What is a simply supported beam?

<choice>
<opt text="A beam where the end portion extends beyond the support.">

This is not the correct answer.

</opt>

<opt text="Beam rests on two supports and is free to move horizontally." correct="true">

Good job!

</opt>

<opt text="a rigid structural element that is supported at one end and free at the other">

This is not correct either.

</opt>
</choice>

</exercise>

<exercise id="3" title="Calculating internal forces of a simply supported beam">

This example shows how to calculate the bending moment and shear of a simply supported beam using `numpy`.

<img src="/beam_example1.png" alt="Simply supported beam image" width="75%">

Given the parameters:

`q=20 kN/m`

`l=5m`

Solution:

First we need to import the numpy library and set the given parameters:

``` python
import numpy as np

q = 20
l = 5
```

We then use the numpy library to create an evenly spaced array betwen 0 to `l`, with a size of 20:

```python
x = np.linspace(0,l,20)
```

Once the array `x` has been generated, we now compute for moment `M` and shear `V`. We just need to write the formula normally in `python` syntax, and `numpy` will apply the formula to all the elements of `x`.

```python
M = q/2*(l*x-x**2)
V = q*(1/2-x)
```

`M `and `V` will have a type of `np.array` and will have the moment and shear at each point of `x`.

Fill in  the code below for yourself and press `Run code` to see the output:

<codeblock id="01_03">

This is a hint.

</codeblock>

</exercise>
