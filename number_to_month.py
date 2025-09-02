def number_to_month(month):
        match month:
                case 1: return "enero"
                case 2: return "febrero"
                case 3: return "marzo"
                case 4: return "abril"
                case 5: return "mayo"
                case 6: return "junio"
                case 7: return "julio"
                case 8: return "agosto"
                case 9: return "septiembre"
                case 10: return "octubre"
                case 11: return "noviembre"
                case 12: return "diciembre"
                case _: return "error"

# No se si era la solucion que buscaban o si querian que usasemos un array pero
# me parecio lo mas practico teniendo en cuenta que son 12 valores exactos y no 
# algo ambiguo

