"""
Smoke test: a minimal end-to-end fit.

Code-heavy, doc-light — test-workspace scripts exercise the code, they do
not teach (that is the workspace's job). This one proves the whole chain
(simulate -> model -> analysis -> search -> result) works against the
installed library, fast enough for CI.
"""

import numpy as np

import autofit as af
import autoproject as ap

truth = ap.Gaussian(centre=30.0, normalization=25.0, sigma=5.0)
data, noise_map = ap.simulate.gaussian_data_with_noise(gaussian=truth, seed=1)

model = af.Model(ap.Gaussian)
analysis = ap.Analysis(data=data, noise_map=noise_map)

search = af.DynestyStatic(name="fit_quick", nlive=30)

result = search.fit(model=model, analysis=analysis)

instance = result.max_log_likelihood_instance

assert np.isfinite(result.log_likelihood)
assert abs(instance.centre - truth.centre) < 5.0, instance.centre

print(f"fit_quick OK: centre={instance.centre:.2f} (truth {truth.centre})")
