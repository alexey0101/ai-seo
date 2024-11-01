import numpy as np


def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))


def layer_norm(x, g, b, eps: float = 1e-5):
    mean = np.mean(x, axis=-1, keepdims=True)
    variance = np.var(x, axis=-1, keepdims=True)
    x = (x - mean) / np.sqrt(
        variance + eps
    )
    return g * x + b


def ffn(x, c_fc, c_proj):
    a = gelu(linear(x, **c_fc))
    x = linear(a, **c_proj)
    return x


def linear(x, w, b):
    return x @ w + b


def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def attention(
    q, k, v, mask
):
    return softmax(q @ k.T / np.sqrt(q.shape[-1]) + mask) @ v


def mha(x, c_attn, c_proj, n_head):
    x = linear(x, **c_attn)
    qkv = np.split(x, 3, axis=-1)
    qkv_heads = list(
        map(lambda x: np.split(x, n_head, axis=-1), qkv)
    )
    causal_mask = (1 - np.tri(x.shape[0])) * -1e10
    out_heads = [
        attention(q, k, v, causal_mask) for q, k, v in zip(*qkv_heads)
    ]
    x = np.hstack(out_heads)
    x = linear(x, **c_proj)
    return x


def transformer_block(
    x, mlp, attn, ln_1, ln_2, n_head
):
    x = x + mha(layer_norm(x, **ln_1), **attn, n_head=n_head)

    x = x + ffn(layer_norm(x, **ln_2), **mlp)

    return x


def gpt2(inputs, wte, wpe, blocks, ln_f, n_head):
    x = wte[inputs] + wpe[range(len(inputs))]

    for block in blocks:
        x = transformer_block(
            x, n_head=n_head, **block
        )

    x = layer_norm(x, **ln_f)
    logits = x @ wte.T

    return logits[-1]
