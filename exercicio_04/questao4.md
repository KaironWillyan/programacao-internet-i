O innerText altera o conteúdo de um elemento de sua página (DOM) com o conteúdo tratado apenas como texto. Por exemplo:

```js
document.getElementById('Teste').innerText = '<b>teste</b>'
```
Irá exibir:

```js
<b>teste<b>
```

Já o innerHTML altera o conteúdo de um elemento com o conteúdo tratado como HTML.

Por exemplo, este código:
```js
document.getElementById('Teste').innerHTML = '<b>teste</b>'
```
Será exibido dessa maneira:

```
teste
```
