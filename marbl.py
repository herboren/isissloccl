import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class DrawMapMarbleOrtho():

    # Draw Marble, pin-point ISS location coords
    def DrawMarble(coords):

        m=Basemap(lat_0=(coords[0]), lon_0=(coords[1]), projection='ortho' )
        m.drawmapboundary(fill_color='#9cc0f9')
        m.fillcontinents(color='#FBF8F3',lake_color='#9cc0f9')
        x, y = m((coords[1]), (coords[0]))
        m.plot(x, y, marker='D', color='dodgerblue', markersize=4, markeredgewidth=1, markeredgecolor='black')
        plt.show()
        m.plot(x, y, marker='D', color='magenta', markersize=4, markeredgewidth=1, markeredgecolor='black')