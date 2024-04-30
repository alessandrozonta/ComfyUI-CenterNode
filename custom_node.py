class BBoxCrop:
    """
    A custom node to compute the top-left coordinates of a cropped bounding box.

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tells the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Return a dictionary which contains config for all input fields.

        Returns: `dict`:
            - Key input_fields_group (`string`): Can be either required, hidden, or optional.
              A node class must have property `required`.
            - Value input_fields (`dict`): Contains input fields config:
                * Key field_name (`string`): Name of an entry-point method’s argument.
                * Value field_config (`tuple`):
                    + First value is a string indicating the type of field or a list for selection.
                    + Second value is a config for type "INT".
        """
        return {
            "required": {
                "left": ("INT"),
                "top": ("INT"),
                "right": ("INT"),
                "bottom": ("INT"),
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