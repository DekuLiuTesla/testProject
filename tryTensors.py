import torch
import numpy as np

# Using Tensors
data = [[1, 2], [3, 4]]  # a list
x_data = torch.tensor(data)  # create directly from data

np_array = np.array(data)
x_np = torch.from_numpy(np_array)  # create from numpy array

# create from another tensor
# print(f"** {expression} **")的方式可以将Python表达式的值添加到字符串内
# retains the properties of x_data, but values are all 1
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

# retains the properties of x_data, but values are all 0
x_zeros = torch.zeros_like(x_data)
print(f"Zeros Tensor: \n {x_zeros} \n")

# overrides the datatype and generate a random float tensor with the same size
x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

# use shape to constrain dimensions
shape = (2, 3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape, dtype=torch.int)
zeros_tensor = torch.zeros(shape)
print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# Attributes of Tensors
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
# if torch.cuda.is_available():
#     tensor = tensor.to('cuda')  # The copy of large tensor across devices can be very time and memory consuming
print(f"Device tensor is stored on: {tensor.device}\n")

# Indexing and Slicing
print("First row: ", tensor[0])
print("First column: ", tensor[:, 0])
print('Last column: ', tensor[..., -1])
tensor[:, 2] = 0
print(tensor, '\n')

# Joining tensors
# .cat()在原有维度中扩展，可以理解为接续，而.stack()会新增一个维度进行叠加
t1 = torch.cat([tensor, tensor, tensor], dim=1)  # cat() or stack()
print(t1, '\n')

# Arithmetic Operations
# Matrix Multiplication in three ways
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(tensor)
torch.matmul(tensor, tensor.T, out=y3)
print(y1)

# Element-wise product
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
print(z1, '\n')

# tensor to one-element tensor to a Python numerical value
agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item), '\n')

# In-place operations
print(tensor, '\n')
tensor.add_(5)
print(tensor)
