body {
    font-family: Arial, sans-serif;
    font-size: 11px;
    background-color: #f0f0f0;
    color: #333333;
}
h1 {
    color: #00a800;
    font-size: 24px;
    font-family: Georgia, serif;
    animation: color-change 3s infinite;
}
/* Animação do título */
@keyframes color-change {
  0%   { color: blue; }
  50%  { color: red; }
  100% { color: blue; }
}
/* Efeito ao passar o mouse no título */
h1:hover {
    transform: scale(1.1);
    transition: 0.3s;
}
/* Estilo da imagem */
img {
    width: 200px;
    transition: transform 0.3s;
}
/* Animação da imagem */
img:hover {
    transform: rotate(5deg) scale(1.1);
}
