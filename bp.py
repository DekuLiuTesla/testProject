import torch

x = torch.ones(5)
y = torch.zeros(3)
w = torch.randn(5, 3, requires_grad=True)  # to be able to compute the gradients of loss function
b = torch.randn(3, requires_grad=True)  # randn is Gaussian, while rand is uniform
z = torch.matmul(x, w) + b  # build a network with one layer
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)  # ???

print("Gradient function for z = ", z.grad_fn)
print("Gradient function for loss = ", loss.grad_fn)

loss.backward()
print(w.grad)
print(b.grad)  # why there's some pattern in the result

print(z.requires_grad)
z_det = z.detach()
print(z_det.requires_grad)
# disable the gradient tracking when you don't need
# then the computational history record and gradient computation support will be stopped
# your can protect parameters and speed up somputation
with torch.no_grad():
    z = torch.matmul(x, w) + b
print(z.requires_grad)

inp = torch.eye(5, requires_grad=True)
out = (inp + 1).pow(2)
out.backward(torch.ones_like(inp), retain_graph=True)
print("First call\n", inp.grad)
out.backward(torch.ones_like(inp), retain_graph=True)
print("Second call\n", inp.grad)
inp.grad.zero_()
out.backward(torch.ones_like(inp), retain_graph=True)
print("\nCall after zeroing gradients\n", inp.grad)
