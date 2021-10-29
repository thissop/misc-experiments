class Asas: 

    def get_images(asas_id): 
        from PIL import Image
        import requests

        map_link = 'http://www.astrouw.edu.pl/cgi-asas/asas_plot_map/'+asas_id+',256,0.0,16.0,0.0,9.99,5,0,asas3'
        map = Image.open(requests.get(map_link, stream=True).raw)
        
        lightcurve_link = 'http://www.astrouw.edu.pl/cgi-asas/asas_plot_raw_all?'+asas_id+',asas3,0,500,0'
        lightcurve_gif = Image.open(requests.get(lightcurve_link, stream=True).raw)
        
        pallete = lightcurve_gif.getpalette()
        
        lightcurve_gif.putpalette(pallete)
        lightcurve = Image.new("RGBA", lightcurve_gif.size)
        lightcurve.paste(lightcurve_gif)

        return map, lightcurve

    def get_lightcurve(): 
        print('hi')

    def get_table(): 
        print('hi')