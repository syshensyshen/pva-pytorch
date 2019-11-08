model_cfg = dict(
    class_list=('__background__',
                'SLD', 'SQ', 'KP', 'WQ', 'YHS', 'SL', 'SLK', 'SLL', 'FC', 'JD', 'SX', 'KQ', 'WC',
                'ZF', 'DJ', 'JG', 'MK'),
    rename_class_list=None,
    ANCHOR_SCALES=[1.2, 2.5, 6, 10, 14, 20, 40],
    ANCHOR_RATIOS=[0.333, 0.5, 0.667, 1, 1.5, 2, 3],
    POOLING_MODE='align',
    POOLING_SIZE=7,
    FEAT_STRIDE=[8],

    model=None,
    save_model_interval=1,

    MODEL=dict(
        RCNN_CIN=512,
        RPN_CIN=512,
        RCNN_LAST=512,
        BACKBONE='shortlitehyper',
        DOUT_BASE_MODEL=336,
    ),

    TRAIN=dict(
        #rpn = dict(),
        #rcnn = dict(),
        dataset="xml",
        train_path=None,
        val_path=None,
        save_dir=None,
        resume_model=None,
        model_name=None,
        gpus=(1, 2, 3,),
        batch_size_per_gpu=12,
        epochs=1000,
        num_works=32,
        LEARNING_RATE=0.001,
        MOMENTUM=0.9,
        WEIGHT_DECAY=0.0005,
        BATCH_SIZE=128,
        FG_FRACTION=0.25,
        FG_THRESH=0.5,
        BG_THRESH_HI=0.5,
        BG_THRESH_LO=0.0,
        RPN_POSITIVE_OVERLAP=0.7,
        RPN_NEGATIVE_OVERLAP=0.3,
        RPN_FG_FRACTION=0.5,
        RPN_BATCHSIZE=256,
        RPN_NMS_THRESH=0.7,
        RPN_PRE_NMS_TOP_N=12000,
        RPN_POST_NMS_TOP_N=2000,
        RPN_BBOX_INSIDE_WEIGHTS=(1.0, 1.0, 1.0, 1.0),
        TRUNCATED=False,
        BBOX_NORMALIZE_MEANS=(0.0, 0.0, 0.0, 0.0),
        BBOX_NORMALIZE_STDS=(0.1, 0.1, 0.2, 0.2),
        BBOX_INSIDE_WEIGHTS=(1.0, 1.0, 1.0, 1.0),
        RPN_MIN_SIZE=8,
        RPN_CLOBBER_POSITIVES=False,
        RPN_POSITIVE_WEIGHT=-1.0,
        BBOX_NORMALIZE_TARGETS_PRECOMPUTED=True,

    ),

    TEST=dict(
        img_path="",
        save_dir="",
        gpus=(3, ),
        SCALES=(600,),
        MAX_SIZE=6400,
        TEST_SCALE=160,
        SCALE_MULTIPLE_OF=32,
        iou_thresh=0.5,
        nms_thresh=0.3,
        thresh=0.6,
        small_object_size=0,
        RPN_PRE_NMS_TOP_N=6000,
        RPN_POST_NMS_TOP_N=300,
        RPN_NMS_THRESH=0.7,
        RPN_MIN_SIZE=8,
        gama=False,
    ),
)