# **Artificial Neural Network (ANNs)**

- Artificial Neural Networks (ANNs) are computational models inspired by the human brain's interconnected neuron structure. They are designed to recognize patterns, make decisions, or learn from data through a set of algorithms.
- It is used to solve both the **classification and Regression** Problem.
- It is used to solve Tabular Data

An ANN is composed of layers of nodes, or neurons:

1. **Input Layer:**
   * **Function:** Receives input data.
   * **Nodes:** Each node represents a feature in the input dataset.
2. **Hidden Layer(s):**
   * **Function:** Intermediary layers that transform input into a form that the output layer can use.
   * **Nodes:** Each hidden layer node applies a function to the input data and passes the output to the subsequent layer. There can be multiple hidden layers, especially in deep learning networks.
3. **Output Layer:**
   * **Function:** Produces the final output of the network.
   * **Nodes:** The number of nodes typically corresponds to the number of classes in a classification task, or a single node in regression tasks.

![1722701600828](./img/ann.jpeg "Author: Arpit Dubey")

### Activation Function ($f(x))$)

* Non-linear transformation applied to the output of a neuron.
* Helps the network learn complex patterns.

**Common Activation Functions:**

* **ReLU (Rectified Linear Unit):** $(f(x) = \max(0, x))$
* **Sigmoid:** ( $f(x)$ = $\frac{1}{1 + e^{-x}}$ )
* **Tanh:** ( $f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ )
* **Softmax:** ( $f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}} $) (typically used in the output layer of classification tasks)

### Loss Function

* Measures the difference between predicted outputs and actual target values.
* Guides the optimization process.

**Common Loss Functions:**

* **Mean Squared Error (MSE):** For regression tasks.
* **Cross-Entropy Loss:** For classification tasks.

### Forward Propagation

**Process:**

1. **Input:** Pass input data through the network.
2. **Hidden Layer Calculation:** Each hidden layer neuron computes a weighted sum of inputs, applies an activation function, and passes the result to the next layer.
3. **Output Layer Calculation:** Processes the data like the hidden layers and produces the final output.

* For a single neuron: $[ z = W \cdot X + b ] $
* $[ a = \sigma(z) ]$
  * Where ( W ) is the weight vector, ( X ) is the input vector, ( b ) is the bias, ( $\sigma$ ) is the activation function, ( z ) is the weighted sum, and ( a ) is the activation.

### Backward Propagation

* Updates the weights to minimize the loss function using gradient descent or a similar optimization method.

**Process:**

1. **Compute Gradient of Loss Function:** Determine the gradient of the loss function with respect to each weight by applying the chain rule.
2. **Weight Update:** Adjust the weights in the opposite direction of the gradient to reduce the loss.

* For a weight $(W_{new}): [ W_{new} = W_{old} - \eta \frac{\partial L}{\partial W_{old}} ]$
  * Where ( $\eta$ ) is the learning rate, and $( \frac{\partial L}{\partial W_{old}} )$ is the gradient of the loss $(L)$ with respect to the weight $( W_{old} )$.

### Necessity of Forward and Backward Propagation

* **Forward Propagation:** Enables the network to compute outputs based on current weights and biases, providing a prediction.
* **Backward Propagation:** Adjusts weights to minimize prediction error, helping the network learn from data.
