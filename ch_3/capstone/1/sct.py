assert 0.70 <= accuracy <= 1.00, "Accuracy should be between 0.70 and 1.00."
assert len(all_preds) == len(all_labels), "Predictions and labels should be concatenated correctly."

Ex().success_msg("All checks passed successfully.")
