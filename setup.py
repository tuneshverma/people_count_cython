from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    # Extension("coco_annotation",  ["coco_annotation.py"]),
    # Extension("centroidtracker",  ["centroidtracker.py"]),
    # Extension("convert",  ["convert.py"]),
    # Extension("kmeans",  ["kmeans.py"]),
    # Extension("model",  ["model.py"]),
    # Extension("people_counter",  ["people_counter.py"]),
    # Extension("train",  ["train.py"]),
    # Extension("train_bottleneck",  ["train_bottleneck.py"]),
    # Extension("utils",  ["utils.py"]),
    # Extension("voc_annotation",  ["voc_annotation.py"]),
    Extension("yolo_counting",  ["yolo_counting.py"]),
    # Extension("trackableobject",  ["trackableobject.py"]),
    #   ... all your modules that need be compiled ...
]
setup(
    name='people_counting',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
