# encoding:utf-8

import config

html = open('saidas/curvaturas/index.html', 'w')

html.write('<html><head><link href="index.css" rel="stylesheet" type="text/css" /></head><body>')

for art in config.artistas:
    path = art.lower()
    html.write('<div class="pintor" id="%s"><h1>%s</h1>' % (art, art))
    for pint in range(5):
        html.write('<h2>Pintura %s de 5</h2>' % (pint+1))
        for k in range(1, 5):
            html.write('<h3>Segmentos %s de 4</h3>' % k)
            html.write('<img class="tratamento" src="%s.tratamento.%s.%s.png"/>' %
                       (path, pint, k))
            html.write('<img class="histpicos" src="%s.histpicos.%s.%s.png" />' %
                       (path, pint, k))
    html.write('</div>')

html.write('</body></html>')
            
            
