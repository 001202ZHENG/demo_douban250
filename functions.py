'''Contain the support functions for the project.'''

from typing import List
def example(x: List[int]) -> List[str]:

from typing import Optional
def example(x:int, y: Optional[bool] = None)
    
def example(x: int = 5, y: float = 2.1)

from typing import Union
def add(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    '''
    Add two numbers.

    Parameters
    ----------
    x : float or int
        The first number to add.
    y : 

    Returns
    -------
    float or int
        The added number

    Examples
    --------
    >>> add(3, 1)
    4
    >>> add(5, 4)
    9
    '''
    return x + y

def divide(x: float, y: float) -> float:
    '''
    Des

    Para

    Return

    Raises
    ------
    ValueError
    '''
    if y == 0:
        raise ValueError("Y cannot be 0.")
    
def load_file():
    pd.read_csv("../data/")