original_output = model(sample_input)
loaded_output = loaded_model(sample_input)
assert torch.allclose(original_output, loaded_output), "Loaded model output should match the original model output."

Ex().success_msg("All checks passed successfully.")
