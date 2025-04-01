{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(['the', 'quick', 'fox'], 'brown'), (['quick', 'brown', 'jumps'], 'fox'), (['brown', 'fox', 'over'], 'jumps'), (['fox', 'jumps', 'the'], 'over'), (['jumps', 'over', 'lazy'], 'the')]\n",
      "[('the', ['quick', 'brown']), ('quick', ['the', 'brown', 'fox']), ('brown', ['the', 'quick', 'fox', 'jumps']), ('fox', ['quick', 'brown', 'jumps', 'over']), ('jumps', ['brown', 'fox', 'over', 'the']), ('over', ['fox', 'jumps', 'the', 'lazy']), ('the', ['jumps', 'over', 'lazy', 'dog']), ('lazy', ['over', 'the', 'dog']), ('dog', ['the', 'lazy']), ('this', ['is', 'another']), ('is', ['this', 'another', 'sentence']), ('another', ['this', 'is', 'sentence']), ('sentence', ['is', 'another'])]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def generate_cbow_data(sentences,window_size):\n",
    "    data=[]\n",
    "    for sentence in sentences:\n",
    "        words=sentence.split()\n",
    "        for i in range(window_size,len(words)-window_size):\n",
    "            target=words[i]\n",
    "            context=words[i-window_size:i]+ words[i+1:i+window_size]\n",
    "            data.append((context,target))\n",
    "    return data\n",
    "\n",
    "def generate_skip_gram_data(sentences,window_size):\n",
    "    data=[]\n",
    "    \n",
    "    for sentence in sentences:\n",
    "        words=sentence.split()\n",
    "        for i in range(len(words)):\n",
    "            target=words[i]\n",
    "            context=[]\n",
    "            for j in range(max(0,i-window_size),min(len(words),i+window_size+1)):\n",
    "                if i!=j:\n",
    "                    context.append(words[j])\n",
    "            data.append((target,context))\n",
    "\n",
    "    return data\n",
    "\n",
    "\n",
    "\n",
    "sentences = ['the quick brown fox jumps over the lazy dog', 'this is another sentence']\n",
    "window_size = 2\n",
    "print(generate_cbow_data(sentences,window_size))\n",
    "print(generate_skip_gram_data(sentences,window_size))\n",
    "\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
