//  Copyright (c) 2021 Intel Corporation
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#ifndef DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_SOFTMAX_HPP_
#define DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_SOFTMAX_HPP_
#include <vector>
#include <string>
#include <unordered_map>
#include "oneapi/dnnl/dnnl.hpp"
#include "../operator.hpp"

namespace executor {
using dnnl::memory;
using dnnl::engine;
using dnnl::prop_kind;
using dnnl::algorithm;

/**
 * @brief A Softmax operator.
 *
 */

class SoftmaxOperator : public Operator {
 public:
  explicit SoftmaxOperator(const OperatorConfig& conf);
  virtual ~SoftmaxOperator() {}

  void Reshape(const vector<Tensor*>& input, const vector<Tensor*>& output) override;
  void Forward(const vector<Tensor*>& input, const vector<Tensor*>& output) override;
  void Prepare(const vector<Tensor*>& input, const vector<Tensor*>& output) override;

 private:
  int axis_;
  string output_dtype_ = "fp32";
  dnnl::engine eng_ = engine(engine::kind::cpu, 0);
  dnnl::softmax_forward softmax_p_;
  memory src_m_;
  memory dst_m_;
  unordered_map<int, memory> memory_args_;

  Tensor* src_ = nullptr;
  Tensor* dst_ = nullptr;

  Tensor* dst_min_ = nullptr;
  Tensor* dst_max_ = nullptr;

  vector<float> dst_scales_;

  void MapTensors(const vector<Tensor*>& input, const vector<Tensor*>& output);
  void Reshape_u8(const vector<Tensor*>& input, const vector<Tensor*>& output);
  void Forward_u8(const vector<Tensor*>& input, const vector<Tensor*>& output);
  void Reshape_f32(const vector<Tensor*>& input, const vector<Tensor*>& output);
  void Forward_f32(const vector<Tensor*>& input, const vector<Tensor*>& output);
};
}  // namespace executor
#endif  // DEEP_ENGINE_EXECUTOR_INCLUDE_OPERATORS_SOFTMAX_HPP_
