import geometry_primitives as geom
import PIL.ImageQt as pilqt

p1 = geom.Point2D([10, 10], pilqt.rgb(0, 0, 0))
p2 = geom.Point2D([20, 20], pilqt.rgb(0, 0, 0))
p3 = geom.Point2D([30, 30], pilqt.rgb(0, 0, 0))

img = geom.Image([p1, p2, p3])
img.draw("test.png")
