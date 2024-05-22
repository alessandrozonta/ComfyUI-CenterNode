class BBoxCrop:
    """
    A custom node for ComfyUI that computes the top-left coordinates of a cropped bounding box given the dimension of the final cropping area.

    Class Methods:
    --------------
    INPUT_TYPES(cls) -> dict:
        A class method returning a dictionary containing configuration for input fields.

    Attributes:
    -----------
    RETURN_TYPES (tuple): 
        Specifies the types of each element in the output tuple.
    FUNCTION (str): 
        The name of the entry-point method.
    CATEGORY (str): 
        Specifies the category the node should appear in the UI.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Returns a dictionary containing configuration for input fields.

        Returns:
        --------
        dict:
            A dictionary with keys specifying input fields and values specifying their types and default values.
        """
        return {
            "required": {
                "left": ("INT", {"default": 0}),
                "top": ("INT", {"default": 0}),
                "right": ("INT", {"default": 100}),
                "bottom": ("INT", {"default": 100}),
                "crop_width": ("INT", {"default": 50}),
                "crop_height": ("INT", {"default": 50})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    FUNCTION = "compute_crop_coordinates"
    CATEGORY = "Custom"

    def compute_crop_coordinates(self, left, top, right, bottom, crop_width, crop_height):
        """
        Computes the top-left coordinates of a cropped bounding box.

        Parameters:
        -----------
        left : int
            The left coordinate of the bounding box.
        top : int
            The top coordinate of the bounding box.
        right : int
            The right coordinate of the bounding box.
        bottom : int
            The bottom coordinate of the bounding box.
        crop_width : int
            The width of the cropped area.
        crop_height : int
            The height of the cropped area.

        Returns:
        --------
        tuple:
            The top-left coordinates of the cropped area.
        """
        bbox_center_x = (left + right) // 2
        bbox_center_y = (top + bottom) // 2

        crop_top_left_x = max(bbox_center_x - crop_width // 2, 0)
        crop_top_left_y = max(bbox_center_y - crop_height // 2, 0)

        return (int(crop_top_left_x), int(crop_top_left_y))

# Dictionary to map node classes to their names
NODE_CLASS_MAPPINGS = {
    "BBoxCrop": BBoxCrop
}

# Dictionary to map node names to their friendly display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "BBoxCrop": "Bounding Box Crop Node"
}
