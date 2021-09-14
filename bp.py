import torch

x = torch.ones(5)
y = torch.zeros(3)
w = torch.randn(5, 3, requires_grad=True)  # to be able to compute the gradients of loss function
b = torch.randn(3, requires_grad=True)  # randn is Gaussian, while rand is uniform
z = torch.matmul(x, w) + b  # build a network with one layer
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)
print("Binary Cross Entropy Loss: ", loss.item())
# it equals to:
# pred = sigmoid(z)
# binary_cross_entropy(pred, y)

# A computation graph consists of Function objects
# grad_fn, as an object, records the function or operation
print("Gradient function for z = ", z.grad_fn)
print("Gradient function for loss = ", loss.grad_fn)

loss.backward()
# only w,b,x,y are leaves(input tensors)
print(w.grad)  # Only leaves with requires_grad=True can show grad
print(b.grad)  # why there's some pattern in the result

# requires_grad == True can be passed through computation
print(z.requires_grad)

# z.detach() creates the same variable as z but with requires_grad=False
z_det = z.detach()
print(z_det.requires_grad)

# disable the gradient tracking when you don't need
# then the computational history record and gradient computation support will be stopped
# your can protect parameters and speed up computation
with torch.no_grad():
    z = torch.matmul(x, w) + b
print(z.requires_grad)

inp = torch.eye(5, requires_grad=True)
out = (inp + 1).pow(2)

# retain_graph=True when you need to backward for several times
# then the computation graph will not be freed
# e.g. when you have multiple loss function
out.backward(torch.ones_like(inp), retain_graph=True)
print("First call\n", inp.grad)

#  PyTorch accumulates the gradients,
#  i.e. the value of computed gradients is added to
#  the grad property of all leaf nodes of computational graph
out.backward(torch.ones_like(inp), retain_graph=True)
print("Second call\n", inp.grad)

# backward() requires parameter when the tensor is non-scalar(have more than one elements)
# to get the Jacobian Product, the input should have the same size as inp
# and the first parameter is in fact the weights of corresponding gradient
inp.grad.zero_()  # set the gradient to be zero
out.backward(torch.ones_like(inp), retain_graph=True)
print("\nCall after zeroing gradients\n", inp.grad)
