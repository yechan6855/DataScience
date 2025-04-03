# ----------------------------------------------------------------------
# import Package
# ----------------------------------------------------------------------
import pandas as pd
import numpy as np
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Combining Datasets: Concat
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

# ----------------------------------------------------------------------

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

# ----------------------------------------------------------------------

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])

# ----------------------------------------------------------------------

x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)

# ----------------------------------------------------------------------

ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])

# ----------------------------------------------------------------------

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display('df1', 'df2', 'pd.concat([df1, df2])')

# ----------------------------------------------------------------------

df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display('df3', 'df4', "pd.concat([df3, df4], axis='columns')")

# ----------------------------------------------------------------------

# example DataFrame
make_df('ABC', range(3))

# ----------------------------------------------------------------------

# Duplicate Indices
x=make_df('AB',[0,1])
y=make_df('AB',[2,3])
y.index=x.index
display('x','y','pd.concat([x,y])')

# ----------------------------------------------------------------------

# 기존 인덱스 제외하고 합치기
display('x', 'y', 'pd.concat([x, y], ignore_index=True)')

# ----------------------------------------------------------------------

display('x','y',"pd.concat([x,y], keys['x','y'])")

# ----------------------------------------------------------------------

df5 = make_df('ABC', [1,2])
df6 = make_df('BCD', [3,4])
print(display('df5', 'df6', 'pd.concat([df5, df6])'))

# ----------------------------------------------------------------------

# 합집합
display('df5','df6',"pd.contact([df5, df6], join='inner')")

# ----------------------------------------------------------------------

