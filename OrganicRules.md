# Rules for Organic Compounds <hr>
## Hydrocarbons
### Alkanes
```python
{
  Name: Prefix + 'ane',
  "Formula": "C(n)H(2n + 2)"
}
```
### Alkenes
```python
{
  Name: Prefix + 'ene',
  "Formula": "C(n)H(2n)"
}
```
### Alkynes
```python
{
  Name: Prefix + 'yne',
  "Formula": "C(n)H(2n - 2)"
}
```
## Alcohols

```python
{
  Name: Prefix + "ol",
  "Formula": "C(n)H(2n + 1)OH"
}
```
## Ethers

```python
{
  Name: [Prefix("Alkyl Group 1") + Prefix("Alkyl Group 2") + "Ether",
        "Di" + Prefix + "Ether"],
  Formula: ["C(n1)H(2n1 + 1)OC(n2)H(2n2 + 1)",
            "C(n)H(2n + 2)O"]
}
```
## Carboxylic Acids
```python
{
  Name: Prefix(+1) + "anoic acid",
  Formula: ["C(n)H(2n + 1)COOH",
            "C(n + 1)H(2n + 2)O2"]
}
```
## Aldehyde
```python
{
  Name: Prefix + "anal",
  Formula: ["C(n)H(2n + 1)CHO",
            "C(n + 1)H(2n + 2)O"]
}
```
## Ketone

```python
{
  Name: [Prefix("Alkyl Group 1") + Prefix("Alkyl Group 2") + "Ketone",
        "Di" + Prefix + "Ketone"],
  Formula: ["C(n1)H(2n1 + 1)COC(n2)H(2n2 + 1)",
            "C(n + 1)H(2n + 2)O"]
}
```
## Esters
```python
{
  Name: Prefix("Alkyl Group") + "yl" + Prefix("Acid Group") + "anoate",
  Formula: ["C(na)H(2na + 1)COOC(nk)H(2nk + 1)",
            "C(n + 1)H(2(n + 1))O2"]
}
```
## Amides
```python
{
  Name: Prefix + "anamide",
  Formula: ["C(n - 1)H(2(n - 1) + 1)CONH2",
            "C(n)H(2n + 1)NO"]
}
```
## Amines
```python
{
  Name: Prefix + "ylamine",
  Formula: ["C(n)H(2n + 1)NH2",
            "C(n)H(2n + 3)N"]
}
```
## Arenes
```python
{
  Name: [Prefix + "benzene",
         "Phenyl" + Prefix],
  Formula: "C(n + 6)H(2n + 6)"
}
```