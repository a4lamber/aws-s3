# for s3 buckets name
variable "bucket_names" {
  type = list(string)
  default = [
    "ehr-raw",
    "ehr-profiling",
    "ehr-basic-filtering",
  ]
}
