# Step 1: Preprocess the CIFAR-10 dataset for training
# (this was completed in the pre-exercise)

# Step 2: Set up a distributed strategy for training the model
with strategy.scope():
    model = build_model()
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])

# Step 3: Train the model using the distributed strategy
history = model.fit(x_train, y_train, epochs=10, 
                    validation_data=(x_test, y_test))

# Step 4: Evaluate the model's performance
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')
