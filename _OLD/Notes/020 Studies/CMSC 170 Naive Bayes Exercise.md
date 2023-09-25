### Please answer the following situations, whether to play golf or not (yes or no). Show your computation.
1. Sunny, Hot, High, True
2. Rainy, Mild, Normal, False
3. Overcast, Cool, Normal, False

---

$P(Play \vert Today) = \frac{P(Outlook \vert Today) \times P(Temperature \vert Today) \times P(Humidity \vert Today) \times P(Wind \vert Today) \times P(Play)}{P(Today)}$

# 1 Sunny | Hot | High | True
$$ P(Yes \vert Today) = \frac{3}{9} \times \frac{2}{9} \times \frac{3}{9} \times \frac{3}{9} \times \frac{9}{14} = 0.00529 $$
$$ P(No \vert Today) = \frac{2}{5} \times \frac{2}{5} \times \frac{4}{5} \times \frac{3}{5} \times \frac{5}{14} = 0.02743 $$

$P(Yes \vert Today) + P(No \vert Today) = 1$
$$ P(Yes \vert Today) = \frac{0.00529}{(0.00529 + 0.02743)} = 0.16167 $$
$$ P(No \vert Today) = \frac{0.02743}{(0.00529 + 0.02743)} = 0.83833 $$
Since $P(No \vert Today) > P(Yes \vert Today)$, the prediction is **No**.

# 2 Rainy | Mild | Normal | False

$$ P(Yes \vert Today) = \frac{2}{9} \times \frac{4}{9} \times \frac{6}{9} \times \frac{6}{9} \times \frac{9}{14} = 0.02822 $$
$$ P(No \vert Today) = \frac{3}{5} \times \frac{2}{5} \times \frac{1}{5} \times \frac{2}{5} \times \frac{5}{14} = 0.00686 $$

$P(Yes \vert Today) + P(No \vert Today) = 1$
$$ P(Yes \vert Today) = \frac{0.02822}{(0.02822 + 0.00686)} = 0.80445 $$
$$ P(No \vert Today) = \frac{0.00686}{(0.02822 + 0.00686)} = 0.1955 $$


Since $P(Yes \vert Today) > P(No \vert Today)$, the prediction is **Yes**.

# 3 Overcast | Cool | Normal | False

$$ P(Yes \vert Today) = \frac{4}{9} \times \frac{3}{9} \times \frac{6}{9} \times \frac{6}{9} \times \frac{9}{14} = 0.04233 $$
$$ P(No \vert Today) = \frac{0}{5} \times \frac{1}{5} \times \frac{1}{5} \times \frac{2}{5} \times \frac{5}{14} = 0 $$

$P(Yes \vert Today) + P(No \vert Today) = 1$
$$ P(Yes \vert Today) = \frac{0.04233}{(0.04233 + 0)} = 1 $$
$$ P(No \vert Today) = \frac{0}{(0.04233 + 0)} = 0 $$

Since $P(Yes \vert Today) > P(No \vert Today)$, the prediction is **Yes**.