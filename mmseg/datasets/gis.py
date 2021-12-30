from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class GISDataset(CustomDataset):
    """GIS dataset.

    In segmentation map annotation for ADE20K, 0 stands for background, which
    is not included in 150 categories. ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = (
        'background',
        'bunker', 'fairway', 'green', 'ground', 'lake', 'tee',
        )

    #PALETTE = [[255, 255, 0], [29, 134, 0], [0, 255, 0], [253, 191, 111], [0, 0, 255], [255, 0, 0]]
    PALETTE = [[0,0,0], [255, 255, 0], [29, 134, 0], [0, 255, 0], [253, 191, 111], [0, 0, 255], [255, 0, 0]]
    #PALETTE = [[0, 255, 255], [0, 134, 29], [0, 255, 0], [111, 191, 253], [255, 0, 0], [0, 0, 255]]

    def __init__(self, **kwargs):
        super(GISDataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
