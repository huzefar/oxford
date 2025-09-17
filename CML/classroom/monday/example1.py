from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd

def main() -> None:
    print("Hello from monday!")
    pd.set_option('display.precision', 2)


if __name__ == "__main__":
    main()