
========= ========= ========= ========= ========= ========= ========= =========
Timings for locmem
-------------------------------------------------------------------------------
   Action     Count      Miss    Median       P90       P99       Max     Total
========= ========= ========= ========= ========= ========= ========= =========
      get    712546    140750  35.048us  56.982us  59.128us  10.045ms  28.172s 
      set     71530         0  36.955us  38.147us  43.154us   9.984ms   2.659s 
   delete      7916         0  31.948us  34.094us  36.001us   9.987ms 267.255ms
    Total    791992                                                    31.099s 
========= ========= ========= ========= ========= ========= ========= =========


========= ========= ========= ========= ========= ========= ========= =========
Timings for memcached
-------------------------------------------------------------------------------
   Action     Count      Miss    Median       P90       P99       Max     Total
========= ========= ========= ========= ========= ========= ========= =========
      get    712546     68969  87.976us 101.089us 113.010us 449.181us  62.615s 
      set     71530         0  92.030us 105.143us 117.779us 442.982us   6.565s 
   delete      7916         0  87.023us  99.897us 113.010us 206.947us 682.936ms
    Total    791992                                                    69.863s 
========= ========= ========= ========= ========= ========= ========= =========


========= ========= ========= ========= ========= ========= ========= =========
Timings for redis
-------------------------------------------------------------------------------
   Action     Count      Miss    Median       P90       P99       Max     Total
========= ========= ========= ========= ========= ========= ========= =========
      get    712546     68854 171.900us 211.000us 250.101us   5.437ms 125.218s 
      set     71530         0 179.052us 216.007us 255.108us   5.327ms  13.051s 
   delete      7916       781 154.018us 190.020us 230.074us   1.309ms   1.253s 
    Total    791992                                                   139.522s 
========= ========= ========= ========= ========= ========= ========= =========


========= ========= ========= ========= ========= ========= ========= =========
Timings for diskcache
-------------------------------------------------------------------------------
   Action     Count      Miss    Median       P90       P99       Max     Total
========= ========= ========= ========= ========= ========= ========= =========
      get    712546     70313  50.068us  67.949us 102.043us  14.113ms  35.382s 
      set     71530         0 355.005us   1.459ms   3.817ms  31.551ms  45.698s 
   delete      7916         0 240.088us   1.330ms   3.665ms  26.498ms   3.785s 
    Total    791992                                                    84.865s 
========= ========= ========= ========= ========= ========= ========= =========


========= ========= ========= ========= ========= ========= ========= =========
Timings for filebased
-------------------------------------------------------------------------------
   Action     Count      Miss    Median       P90       P99       Max     Total
========= ========= ========= ========= ========= ========= ========= =========
      get    712580    123599  97.990us 144.958us 257.015us  15.342ms  75.490s 
      set     71539         0   5.274ms   6.261ms   7.501ms  26.983ms 376.789s 
   delete      7873         0 139.952us 235.081us 398.874us   1.394ms   1.218s 
    Total    791992                                                   453.496s 
========= ========= ========= ========= ========= ========= ========= =========
