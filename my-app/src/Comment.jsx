import anon from './anon.jpg';

const Comment = ({ id, author, text, date, likes, image }) => {
    const dt = new Date(date);
    const options = {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true,
        timeZone: 'UTC', 
    };
    const formatDate = dt.toLocaleDateString('en-US', options);

    const containerStyle = {
        maxWidth: '400px',
        border: '1px solid #ddd',
        borderRadius: '12px',
        padding: '16px',
        margin: '16px auto',
        boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
        fontFamily: 'Arial, sans-serif',
    };

    const headerStyle = {
        display: 'flex',
        gap: '12px',
        marginBottom: '12px',
    };

    const imgStyle = {
        width: '96px',
        height: '96px',
        objectFit: 'cover',
        borderRadius: '8px',
    };

    const authorInfoStyle = {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
    };

    const textStyle = {
        fontSize: '14px',
        marginBottom: '12px',
        color: '#333',
    };

    const footerStyle = {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
    };

    const buttonStyle = {
        padding: '4px 10px',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        fontSize: '12px',
        marginLeft: '6px',
    };

    const likeButton = {
        ...buttonStyle,
        backgroundColor: '#e0f2fe',
        color: '#0369a1',
    };

    const dislikeButton = {
        ...buttonStyle,
        backgroundColor: '#fee2e2',
        color: '#b91c1c',
    };

    const actionButtonStyle = {
        ...buttonStyle,
        backgroundColor: '#f3f4f6',
        color: '#333',
    };

    return (
        <div style={containerStyle}>
            <div style={headerStyle}>
                <img src={image ? image : anon} alt={`${author}'s profile`} style={imgStyle} />
                <div style={authorInfoStyle}>
                    <span style={{ fontWeight: 'bold' }}>@{author}</span>
                    <span style={{ fontSize: '12px', color: '#777' }}>{formatDate}</span>
                </div>
            </div>

            <div style={textStyle}>{text}</div>

            <div style={footerStyle}>
                <span style={{ fontSize: '12px', color: '#555' }}>{likes} likes</span>

                <div>
                    <button style={actionButtonStyle}>Edit</button>
                    <button style={actionButtonStyle}>Delete</button>
                </div>
            </div>
        </div>
    );
};

export default Comment;
